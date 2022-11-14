from .models import Game,GameSquare
from rest_framework import serializers



class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'winner', 'creator', 'opponent', 'cols', 
                  'rows', 'completed', 'created', 'current_turn')
        depth = 1
 
 
class GameSquareSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameSquare
        fields = ('id', 'game', 'owner', 'status', 'row', 'col')