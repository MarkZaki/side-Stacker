# chat/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Connect4Game

user_id_string = 'user_id'

class Connect4Consumer(WebsocketConsumer):

    def connect(self):      
        self.game_id = self.scope['url_route']['kwargs']['game_id']
        self.game_name = 'game_%s' % self.game_id #just string formatting

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.game_name,
            self.channel_name
        )

        #TODO set boolean for players connected; but many connection can be made at same time
        #set up/get game
        game = Connect4Game.objects.get(pk = self.game_id)
        if game.player1 == self.scope['cookies'][user_id_string]:
            self.PlayerNum = 1 
            game.numPlayer1Connections += 1
        elif game.player2 == self.scope['cookies'][user_id_string]:
            self.PlayerNum = 2
            game.numPlayer2Connections += 1
        else:
            self.send({"close": True}) #closes the connection immediately
        game.save()   
        self.accept()
        self._makeEveryoneUpdate()

    def disconnect(self, close_code):
        game = Connect4Game.objects.get(pk = self.game_id)
        if self.PlayerNum == 1:
            game.numPlayer1Connections -= 1
        elif self.PlayerNum == 2:
            game.numPlayer2Connections -= 1
        else:
            Exception("PlayerNum must be 1 or 2")
        game.save()
        self._makeEveryoneUpdate()
        async_to_sync(self.channel_layer.group_discard)(
            self.game_name,
            self.channel_name
        )

    #tells everone in group to update
    def _makeEveryoneUpdate(self):
        async_to_sync(self.channel_layer.group_send)(
            self.game_name,
            {
                'type': 'update_message'
            }
        )

    #recieve message from websocket
    def receive(self, text_data):
        # print(text_data)
        text_data_json = json.loads(text_data)
        row  = text_data_json['row']
        side = text_data_json['side']
        player = text_data_json['player'] 
        game = Connect4Game.objects.get(pk = self.game_id) 
        if not game.TryMove(player,row,side):
            print("Move was not allowed")
        self._makeEveryoneUpdate() 

    # Receive message from other player
    def update_message(self, event):
        self._sendToClient()

    def _sendToClient(self):
        game = Connect4Game.objects.get(pk = self.game_id)
        gameToSend = {}
        gameToSend['board'] = game.game_state
        gameToSend['player'] = self.PlayerNum
        opponentConnected = False
        if self.PlayerNum == 1:
            opponentConnected = game.numPlayer2Connections >= 1
        if self.PlayerNum == 2:
            opponentConnected = game.numPlayer1Connections >= 1
        gameToSend['opponentConnected'] = opponentConnected
        self.send(text_data=json.dumps(gameToSend))