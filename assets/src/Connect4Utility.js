/*input is a board
  7x6 or colxrow
  0 -> empty
  1 -> player 1
  2 -> player 2

  output
  0 -> no winner
  1 -> player one wins
  2 -> player 2 wins
  3 -> tie
*/
export function IsWinner(board) {
  const vertical = {
    colStart: 0,
    col: 7,
    row: 3,
    colIncrement: [0, 0, 0],
    rowIncrement: [1, 2, 3],
  };
  const horizontal = {
    colStart: 0,
    col: 4,
    row: 6,
    colIncrement: [1, 2, 3],
    rowIncrement: [0, 0, 0],
  };
  const downRightDiagonal = {
    colStart: 0,
    col: 4,
    row: 3,
    colIncrement: [1, 2, 3],
    rowIncrement: [1, 2, 3],
  };

  const downLeftDiagonal = {
    colStart: 3,
    col: 7,
    row: 3,
    colIncrement: [-1, -2, -3],
    rowIncrement: [1, 2, 3],
  };

  const checks = [vertical, horizontal, downRightDiagonal, downLeftDiagonal];
  for (const check of checks) {
    for (let col = check.colStart; col < check.col; col++) {
      for (let row = 0; row < check.row; row++) {
        const possibleWinner = CheckWinner(
          board[col][row],
          board[col + check.colIncrement[0]][row + check.rowIncrement[0]],
          board[col + check.colIncrement[1]][row + check.rowIncrement[1]],
          board[col + check.colIncrement[2]][row + check.rowIncrement[2]]
        );
        if (possibleWinner !== 0) {
          return possibleWinner;
        }
      }
    }
  }

  //if all spaces filled up then tie
  const isBoardFull = board.filter((col) => !IsColumnFull(col)).length == 0;
  if (isBoardFull) {
    return 3;
  }
  return 0;
}

//true if column filled up
export function IsColumnFull(col) {
  return col.every((space) => space != 0);
}

/*checks if there is a winner for 4 consecitive pieces
  input -> pieces have 0,1,2
  returns   
  0 -> no winner
  1 -> player one wins
  2 -> player 2 wins
*/
export function CheckWinner(firstPiece, secondPiece, thirdPiece, forthPiece) {
  if (
    firstPiece === secondPiece &&
    firstPiece === thirdPiece &&
    firstPiece === forthPiece
  ) {
    return firstPiece;
  }
  return 0;
}

/*
  determines if it is the player's turn or not
  input: normal connect 4 board defined above, player -> 1 or 2
  output: true if it is the players turn
*/
export function IsTurn(board, player) {
  //TODO No your turn if game is over
  let arrayOfSum = board.map((arr) => arr.reduce(countNonZeros, 0)); //0 makes it start at 0
  let sum = arrayOfSum.reduce(sumReducer);
  return sum % 2 == player - 1;
}

const countNonZeros = (accumulator, currentValue) =>
  accumulator + (currentValue == 0 ? 0 : 1);
const sumReducer = (accumulator, currentValue) => accumulator + currentValue;
