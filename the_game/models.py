from django.db import models
import jsonfield
import numpy as np
from .Connect4Utility import IsTurn

# PlayerKeyMaxLength = 50

class Connect4Game(models.Model):
    def initilizeBoard():
        #board is 6X7
        #the first index is col: 0 is left most row, 6 if right row
        #the second index is the row: 0 is the top row: 5 is the bottom row
        return [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]


    game_state = models.JSONField(default =initilizeBoard)
    player1 = models.CharField(max_length = 100, default='')
    player2 = models.CharField(max_length = 100, default='')
    numPlayer1Connections = models.IntegerField(default=0)
    numPlayer2Connections = models.IntegerField(default=0) 


    def TryMove(self, player, row,side):
        if IsTurn(self.game_state, player):
            row_value = self.game_state[row] #ex row 0 [0,0,0,0,0,0,0] has 7 0s which are cols
            index = -1
            if side == 'Right':
                for col in reversed(row_value):
                    if col == 0 :
                        index += 1
                if index == -1:
                    #row full
                    print("row is full")
                    return False
                row_value[index] = player
                self.game_state[row] = row_value
                self.save()
                return True
            elif side == 'Left':
                for col in row_value:
                    if col == 0 :
                        index += 1
                if index == -1:
                    print("row is full")
                    return False
                row_value[index] = player 
                self.game_state[row] = row_value
                self.save()
                return True
            return False