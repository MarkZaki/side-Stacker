def check_winner(board,player):
    """
    takes a player and the board then it will check the winning conditions 
    and the reverse of those since we are checking both sides 
    it will return 
    0 - means still no winner so keep the game going 
    1 -  player one won stop the game and set it as complete
    2 -  player two won stop the game and set it as complete
    TODO  check for Tie  return 3
    """
    coulmn_count = 7
    row_count = 7
    reversed_board = []
    for row in board:
        row = list(reversed(row))
        reversed_board.append(row)
    # horizontal check
    for r in range (row_count):
        for c in range(coulmn_count-3):
            if board[r][c] == player and board[r][c+1] == player and board[r][c+2] == player and board[r][c+3] == player:
                return player
            elif reversed_board[r][c] == player and reversed_board[r][c+1] == player and reversed_board[r][c+2] == player and reversed_board[r][c+3] == player:
                return player
    # vertical check
    for r in range (row_count-3):
        for c in range(coulmn_count):
            if board[r][c] == player and board[r+1][c] == player and board[r+2][c] == player and board[r+3][c] == player:
                return player
            elif reversed_board[r][c] == player and reversed_board[r+1][c] == player and reversed_board[r+2][c] == player and reversed_board[r+3][c] == player:
                return player
    # diagonal / check
    for r in range (row_count-3):
        for c in range(coulmn_count-3):
            if board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player and board[r+3][c+3] == player:
                return player
            elif reversed_board[r][c] == player and reversed_board[r+1][c+1] == player and reversed_board[r+2][c+2] == player and reversed_board[r+3][c+3] == player:
                return player
    # diagonal \ check
    for r in range (2,row_count):
        for c in range(coulmn_count-3):
            if board[r][c] == player and board[r-1][c+1] == player and board[r-2][c+2] == player and board[r-3][c+3] == player:
                return player
            elif reversed_board[r][c] == player and reversed_board[r-1][c+1] == player and reversed_board[r-2][c+2] == player and reversed_board[r-3][c+3] == player:
                return player
    else:
        return 0
    pass
    




def IsTurn(game, player):
    '''
    determines if it is the player's turn or not
    input: normal connect 4 board defined above, player -> 1 or 2
    output: true if it is the players turn
    since we always start with player1 so depending on the number or peicecs 
    starts at 0 if the number is even that means its player1's turn if its odd then its player2's turn
    '''
    if game.game_complete:
        return False
    board = game.game_state
    numberOfPiecesOnBoard = 0

    for col in board:
        for piece in col:
            if not piece == 0:
                numberOfPiecesOnBoard += 1
            else:
                pass
    return numberOfPiecesOnBoard % 2 == player - 1 # returns boolean