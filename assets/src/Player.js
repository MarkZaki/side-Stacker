import React from "react";

/*
props expected:
 {
    "isTurn: boolean,
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
  if (props.isTurn && props.areYouThisPlayer) {
    moveDescription = <h4> Your Turn </h4>;
  }

  if (!props.isTurn && !props.areYouThisPlayer) {
    moveDescription = <h4> Their Turn </h4>;
  }

  return (
    <div className="player">
      {icon}
      {playerTitle}
      {moveDescription}
    </div>
  );
}
