import React from "react";
import Column from "./Column";
import { IsTurn } from "./Connect4Utility";

function Board(props) {
  let counter = -1;
  const columns = props.board.map((col) => {
    counter += 1;
    return (
      <Column
        player={props.player}
        isTurn={IsTurn(props.board, props.player)}
        value={col}
        key={counter}
        colNum={counter}
        clickHandler={props.SendMove}
      />
    );
  });
  return (
    <div className="board" data-testid="game">
      {columns}
    </div>
  );
}

export default Board;
