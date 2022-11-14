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
            row_value = self.game_state[row] #ex row 0 [1,0,0,0,0,0,0] has 7 0s which are cols
            if side == 'Right':
                # print("adding to the right")
                index = -1
                for elem_number,col in reversed(list(enumerate(row_value))):
                    if col == 0 :
                        # print('-------------------')
                        # print('colvalue',col)
                        # print('colindex',elem_number)
                        # print('index',index)
                        # print('-------------------')
                        index += 1
                        break
                if index == -1:
                    #row full
                    print("row is full")
                    return False
                # print('inserting in index num',elem_number)
                # try
                row_value.pop(elem_number)
                row_value.append (player)
                self.game_state[row] = row_value
                self.save()
                # index = -1
                return True
            elif side == 'Left':
                # print("adding to the righ")
                index = -1
                for elem_number,col in list(enumerate(row_value)):
                    # print('-------------------')
                    # print('col',col)
                    # print('colindex',elem_number)
                    # print('index',index)
                    # print('-------------------')
                    if col == 0 :
                        index += 1
                        break
                if index == -1:
                    print("row is full")
                    return False
                # print('inserting in index num',elem_number)
                row_value.pop(elem_number)
                row_value.insert(0,player )
                self.game_state[row] = row_value
                self.save()
                # index = -1
                return True
            return False