from django.contrib.auth.models import User
from django.db import models
from asgiref.sync import async_to_sync
import json
from datetime import datetime
from channels.layers import get_channel_layer
class Game(models.Model):
    """
    This is a game of connec 4 between two players.
    Initial values when created will just be a creator
    who is also the current_turn and the cols and rows
    """
    # main fields
    creator = models.ForeignKey(User, related_name='creator',on_delete=models.CASCADE)
    opponent = models.ForeignKey(
        User, related_name='opponent', null=True, blank=True,on_delete=models.CASCADE)
    winner = models.ForeignKey(
        User, related_name='winner', null=True, blank=True,on_delete=models.DO_NOTHING)
    cols = models.IntegerField(default=7)
    rows = models.IntegerField(default=7)
    current_turn = models.ForeignKey(User, related_name='current_turn',on_delete=models.CASCADE)
 
    # dates
    completed = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return 'Game #{0}'.format(self.pk)
 
    @staticmethod
    def get_available_games():
        return Game.objects.filter(opponent=None, completed=None)
 
    @staticmethod
    def created_count(user):
        return Game.objects.filter(creator=user).count()
    # where the user was the oppnent or a creator 
    @staticmethod
    def get_games_for_player(user):
        from django.db.models import Q
        return Game.objects.filter(Q(opponent=user) | Q(creator=user))
 
    @staticmethod
    def get_by_id(id):
        try:
            return Game.objects.get(pk=id)
        except Game.DoesNotExist:
            # TODO: Handle this Exception
            pass
 
    @staticmethod
    def create_new(user):
        """
        Create a new game and game squares
        :param user: the user that created the game
        :return: a new game object
        """
        # make the game's name from the username and the number of
        # games they've created
        new_game = Game(creator=user, current_turn=user)
        new_game.save()
        # for each row, create the proper number of cells based on cols
        for row in range(new_game.rows):
            for col in range(new_game.cols):
                new_square = GameSquare(
                    game=new_game,
                    row=row,
                    col=col
                )
                new_square.save()
        return new_game
 
 
    def get_all_game_squares(self):
        """
        Gets all of the squares for this Game
        """
        return GameSquare.objects.filter(game=self)
 
    def get_game_square(self,row, col):
        """
        Gets a square for a game by it's row and col pos
        """
        try:
            return GameSquare.objects.get(game=self, cols=col, rows=row)
        except GameSquare.DoesNotExist:
            return None
 
    def get_square_by_coords(self, coords):
        """
        Retrieves the cell based on it's (x,y) or (row, col)
        """
        try:
            square = GameSquare.objects.get(row=coords[1],
                                            col=coords[0],
                                            game=self)
            return square
        except GameSquare.DoesNotExist:
            # TODO: Handle exception for gamesquare
            return None
    
    def send_game_update(self):
        """
        Send the updated game information and squares to the game's channel group
        """
        # imported here to avoid circular import
        from serializers import GameSquareSerializer, GameSerializer
        channel_layer = get_channel_layer()
 
        squares = self.get_all_game_squares()
        square_serializer = GameSquareSerializer(squares, many=True)

 
        game_serilizer = GameSerializer(self)
 
        message = {'game': game_serilizer.data,
                   'squares': square_serializer.data}
 
        game_group = 'game-{0}'.format(self.id)
        async_to_sync(channel_layer.send)(game_group, {'text': json.dumps(message)})
        # Group(game_group).send({'text': json.dumps(message)})
 
    def next_player_turn(self):
        """
        Sets the next player's turn
        """
        if self.current_turn != self.creator:
            self.current_turn = self.creator
            self.save()
        else:
            self.current_turn = self.opponent
            self.save()
 
    def mark_complete(self, winner):
        """
        Sets a game to completed status and records the winner
        """
        self.winner = winner
        self.completed = datetime.now()
        self.save()
 
 
class GameSquare(models.Model):
    STATUS_TYPES = (
        ('Free', 'Free'),
        ('Selected', 'Selected'),
        ('Surrounding', 'Surrounding')
    )
    game = models.ForeignKey(Game,on_delete=models.CASCADE)
    owner = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_TYPES,
                              max_length=25,
                              default='Free')
    row = models.IntegerField()
    col = models.IntegerField()
 
    # dates
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
 
    def __unicode__(self):
        return '{0} - ({1}, {2})'.format(self.game, self.col, self.row)
 
    @staticmethod
    def get_by_id(id):
        try:
            return GameSquare.objects.get(pk=id)
        except GameSquare.DoesNotExist:
            # TODO: Handle exception for gamesquare
            return None
 
    def get_surrounding(self):
        """
        Returns this square's surrounding neighbors that are still Free
        """
        ajecency_matrix = [(i, j) for i in (-1, 0, 1)
                           for j in (-1, 0, 1) if not (i == j == 0)]
        results = []
        for dx, dy in ajecency_matrix:
            # boundaries check
            if 0 <= (self.col + dy) < self.game.cols and 0 <= self.row + dx < self.game.rows:
                results.append((self.col + dy, self.row + dx))
        return results
 
    def claim(self, status_type, user):
        """
        Claims the square for the user
        """
        self.owner = user
        self.status = status_type
        self.save(update_fields=['status', 'owner'])
 
        # get surrounding squares and update them if they can be updated
        surrounding = self.get_surrounding()
 
        for coords in surrounding:
            # get square by coords
            square = self.game.get_square_by_coords(coords)
 
            if square and square.status == 'Free':
                square.status = 'Surrounding'
                square.owner = user
                square.save()
 
 
        # set the current turn for the other player if there are still free
        # squares to claim
        if self.game.get_all_game_squares().filter(status='Free'):
            self.game.next_player_turn()
        else:
            self.game.mark_complete(winner=user)
        # let the game know about the move and results
        self.game.send_game_update()