from django.test import TestCase
from the_game.game_utility import check_winner, is_turn
# Create your tests here.


class IsWinnerTests(TestCase):

    def board_is_empty_no_win(self):
        board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        self.assertEqual(check_winner(board), 0)
    
    def horizontal_win_right(self):
        board = [[0,0,0,0,0,0,0],[0,0,0,1,1,1,1],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        self.assertEqual(check_winner(board), 1)
        
    def horizontal_win_left(self):
        board = [[0,0,0,0,0,2,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[2,2,2,2,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        self.assertEqual(check_winner(board), 2)
        
    def vertical_win(self):
        board = [[0,0,0,0,0,2,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[2,0,0,0,0,0,0],[2,2,2,0,0,0,0],[2,0,0,0,0,0,0],[2,0,0,0,0,0,0]]
        self.assertEqual(check_winner(board), 2)

    def diagonal_win(self):
        board = [[1,0,0,0,0,2,0],[2,1,0,1,0,0,0],[2,2,1,0,0,0,0],[1,1,2,1,0,0,0],[2,2,2,0,0,0,0],[1,0,0,0,0,0,0],[2,0,0,0,0,0,0]]
        self.assertEqual(check_winner(board), 1)

    def other_diagonal_win(self):
        board = [[0,0,0,0,0,2,1],[0,0,0,0,0,1,2],[0,0,0,0,1,0,0],[1,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        self.assertEqual(check_winner(board), 1)
    #TODO tie is almost imposible to happen 
