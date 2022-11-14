from django.test import TestCase
from .Connect4Utility import IsWinner, IsTurn
# Create your tests here.


class IsWinnerTests(TestCase):

    def test_IsWinner_Empty(self):
        board = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        self.assertEqual(IsWinner(board), 0)

    def test_IsWinner_Tie(self):
        board = [[1,1,1,2,2,2],[2,2,2,1,1,1],[1,1,1,2,2,2],[2,2,2,1,1,1],[1,1,1,2,2,2],[2,2,2,1,1,1],[1,1,1,2,2,2]]
        self.assertEqual(IsWinner(board), 3)

    def test_IsWinner_NoWinnerAlmostFull(self):
        board = [[1,1,1,2,2,2],[2,2,2,1,1,1],[1,1,1,2,2,2],[0,2,2,1,1,1],[1,1,1,2,2,2],[2,2,2,1,1,1],[1,1,1,2,2,2]]
        self.assertEqual(IsWinner(board), 0)

    def test_IsWinner_NoWinnerBottomRowFull(self):
        board = [[0,0,0,0,0,1],[0,0,0,0,0,2],[0,0,0,0,0,1],[0,0,0,0,0,2],[0,0,0,0,0,1],[0,0,0,0,0,2],[0,0,0,0,0,1]]
        self.assertEqual(IsWinner(board), 0)

    def test_IsWinner_NoWinnerRightColFull(self):
        board = [[2,1,2,1,2,1],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        self.assertEqual(IsWinner(board), 0)

    def test_IsWinner_NoWinner_ModeratlyEmpty(self):
        board = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,2],[0,0,0,0,0,2],[0,0,0,1,1,1],[0,0,0,0,0,0]]
        self.assertEqual(IsWinner(board), 0)

    def test_IsWinner_VerticalPlayer1(self):
        board = [[0,0,1,1,1,1],[0,0,0,0,0,0],[0,0,0,0,0,2],[0,0,0,0,0,2],[0,0,0,0,0,2],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        self.assertEqual(IsWinner(board), 1)

    def test_IsWinner_VerticalPlayer1TopRow(self):
        board = [[1,1,1,1,0,0],[0,0,0,0,0,0],[0,0,0,0,0,2],[0,0,0,0,0,2],[0,0,0,0,0,2],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        self.assertEqual(IsWinner(board), 1)

    def test_IsWinner_VerticalPlayer2(self):
        board = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,2,2,2,2],[0,0,0,0,1,1],[0,0,0,0,1,1],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        self.assertEqual(IsWinner(board), 2)

    def test_IsWinner_VerticalPlayer2TopRow(self):
        board = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,1,1],[0,0,0,0,1,1],[0,0,0,0,0,0],[0,0,2,2,2,2]]
        self.assertEqual(IsWinner(board), 2)

    def test_IsWinner_HorizontalPlayer1(self):
        board = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,1],[0,0,0,0,1,1],[0,0,0,0,1,1],[0,0,0,0,0,1],[0,0,1,2,2,2]]
        self.assertEqual(IsWinner(board), 1)

    def test_IsWinner_HorizontalPlayer2Win(self):
        board = [[2,0,0,0,0,0],[2,0,0,0,0,0],[2,0,0,0,0,0],[2,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        self.assertEqual(IsWinner(board), 2)        

    def test_IsWinner_DownRightPlayer1(self):
        board = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]]
        self.assertEqual(IsWinner(board), 1)     

    def test_IsWinner_DownRightPlayer2(self):
        board = [[2,0,0,0,0,0],[0,2,0,0,0,0],[0,0,2,0,0,0],[0,0,0,2,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]]
        self.assertEqual(IsWinner(board), 2)     

    def test_IsWinner_DownRightPlayer2Lower(self):
        board = [[0,0,2,0,0,0],[0,0,0,2,0,0],[0,0,0,0,2,0],[0,0,0,0,0,2],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]]
        self.assertEqual(IsWinner(board), 2)  

    def test_IsWinner_DownLeftPlayer1(self):
        board = [[0,0,0,1,0,0],[0,0,1,0,0,0],[0,1,0,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        self.assertEqual(IsWinner(board), 1)  

    def test_IsWinner_DownLeftPlayer2(self):
        board = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,2],[0,0,0,0,2,0],[0,0,0,2,0,0],[0,0,2,0,0,0]]
        self.assertEqual(IsWinner(board), 2) 

class IsTurnTests(TestCase):

    def test_IsTurnEmptyPlayer1(self):
        board = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        player = 1
        self.assertEqual(IsTurn(board, player), True)


    def test_IsTurnEmptyPlayer2(self):
        board = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        player = 2
        self.assertEqual(IsTurn(board, player), False)

    def test_IsTurn3MovesInPlayer2(self):
        board = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,2,1],[0,0,0,0,0,1],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        player = 2
        self.assertEqual(IsTurn(board, player), True)

    def test_IsTurn3MovesInPlayer1(self):
        board = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,2,1],[0,0,0,0,0,1],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        player = 1
        self.assertEqual(IsTurn(board, player), False)

    def test_IsTurnLastMovePlayer1(self):
        board = [[1,1,1,2,2,2],[2,2,2,1,1,1],[1,1,1,2,2,2],[0,2,2,1,1,1],[1,1,1,2,2,2],[2,2,2,1,1,1],[1,1,1,2,2,2]]
        player = 1
        self.assertEqual(IsTurn(board, player), False)

    def test_IsTurnLastMovePlayer2(self):
        board = [[1,1,1,2,2,2],[2,2,2,1,1,1],[1,1,1,2,2,2],[0,2,2,1,1,1],[1,1,1,2,2,2],[2,2,2,1,1,1],[1,1,1,2,2,2]]
        player = 2
        self.assertEqual(IsTurn(board, player), True)


    def test_IsTurnTiePlayer2(self):
        board = [[1,1,1,2,2,2],[2,2,2,1,1,1],[1,1,1,2,2,2],[2,2,2,1,1,1],[1,1,1,2,2,2],[2,2,2,1,1,1],[1,1,1,2,2,2]]
        player = 2
        self.assertEqual(IsTurn(board, player), False)

    def test_IsTurnTiePlayer1(self):
        board = [[1,1,1,2,2,2],[2,2,2,1,1,1],[1,1,1,2,2,2],[2,2,2,1,1,1],[1,1,1,2,2,2],[2,2,2,1,1,1],[1,1,1,2,2,2]]
        player = 1
        self.assertEqual(IsTurn(board, player), False)

    def test_IsTurnLosePlayer2(self):
        board = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,2,1],[0,0,0,0,2,1],[0,0,0,0,2,1],[0,0,0,0,0,1]]
        player = 2
        self.assertEqual(IsTurn(board, player), False)

    def test_IsTurnLosePlayer1(self):
        board = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,2,1],[0,0,0,0,2,1],[0,0,0,0,2,1],[0,1,1,1,2,2]]
        player = 2
        self.assertEqual(IsTurn(board, player), False)
