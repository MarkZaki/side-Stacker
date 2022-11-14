def IsWinner(board):
    '''
    input is a board
    7x7 or colxrow, python arrays
    below are the cells 
    0 -> empty
    1 -> player 1
    2 -> player 2

    output
    0 -> no winner ( default state so the game can keep going )
    1 -> player one wins
    2 -> player two wins
    3 -> tie
    '''
    upper = {
        "colStart": 0,
        "col": 4,
        "row": 3,
        "colIncrement": [1,2,3],
        "rowIncrement": [1,2,3]
    }

    lower = {
        "colStart" : 3,
        "col": 7,
        "row": 3,
        "colIncrement": [-1,-2,-3],
        "rowIncrement": [1,2,3]
    }

    checks = [upper, lower]

    for check in checks:
        for col in range(check["colStart"], check["col"]):
            for row in range(check["row"]):
                possibleWinner = CheckWinner(
                    board[col][row],
                    board[col + check["colIncrement"][0]][row + check["rowIncrement"][0]],
                    board[col + check["colIncrement"][1]][row + check["rowIncrement"][1]],
                    board[col + check["colIncrement"][2]][row + check["rowIncrement"][2]])
                if possibleWinner != 0:
                    return possibleWinner
                
    topRow = [col[0] for col in board]
    isBoardFull = sum([1 if piece == 0 else 0 for piece in topRow]) == 0
    if isBoardFull:
        return 3
    return 0
  

def CheckWinner(firstPiece, secondPiece, thirdPiece, forthPiece):
    '''
    checks if there is a winner for 4 consecitive pieces
    input -> pieces have 0,1,2
    returns   
    0 -> no winner
    1 -> player one wins
    2 -> player 2 wins
    '''
    
    if(firstPiece == secondPiece and firstPiece == thirdPiece and firstPiece == forthPiece):
        return firstPiece
    return 0



def IsTurn(board, player):
    '''
    determines if it is the player's turn or not
    input: normal connect 4 board defined above, player -> 1 or 2
    output: true if it is the players turn
    '''
    #check if there is a winner before every turn 
    if IsWinner(board) != 0:
        return False 
    #means there are still no winners yet 
    numberOfPiecesOnBoard = 0
    # will check every cell of every column if its not empty will add one to the num of pieces else will pass
    for col in board:
        for piece in col:
            if not piece == 0:
                numberOfPiecesOnBoard += 1
            else:
                pass
    #since we always start with player one so depending on the number or peicecs starts at 0 if the number is even 
    #that means its player1's turn if its odd then its player2's turn
    return numberOfPiecesOnBoard % 2 == player - 1 # returns boolean