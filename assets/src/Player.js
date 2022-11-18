import React from "react";

/*
props expected:
 {
    "is_turn: boolean,
    "isPlayer1": boolean,
    "areYouThisPlayer", boolean,
}
*/
export default function Player(props) {
  let icon;
  let playerTitle;
  if (props.isPlayer1) {
    icon = (
      <ion-icon
        name="person-outline"
        className="icon-person icon-player1"
      ></ion-icon>
    );
    playerTitle = <h3 className="player-title">Player 1</h3>;
  } else {
    icon = (
      <ion-icon
        name="person-outline"
        className="icon-person icon-player2"
      ></ion-icon>
    );
    playerTitle = <h3 className="player-title"> Player 2</h3>;
  }

  let moveDescription = null;
  if (props.is_turn && props.areYouThisPlayer) {
    moveDescription = <h4> Your Turn </h4>;
  } else {
    moveDescription = <h4> Their Turn </h4>;
  }

  return (
    <div className="player">
      <div
        className="card"
        style={{
          background: props.areYouThisPlayer ? "#f1c40f" : "#ecf0f1",
          boxShadow: props.is_turn
            ? "rgba(255, 255, 255, 0.397) 0px 15px 29px 0px"
            : null,
        }}
      >
        <div className="card-header">
          {icon}
          {playerTitle}
        </div>
      </div>
    </div>
  );
}
