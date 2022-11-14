import React from "react";
import Board from "./Board";
import { w3cwebsocket as W3CWebSocket } from "websocket";
import { IsTurn, IsWinner } from "./Connect4Utility.js";
import Player from "./Player";

const game_id = document.getElementById("game_id").textContent;
const game_link = document.getElementById("game_link").textContent;
const client = new W3CWebSocket(
  "ws://" + window.location.host + "/ws/" + game_id + "/"
);

class App extends React.Component {
  constructor() {
    super();
    this.state = {};
    this.SendMove = this.SendMove.bind(this);
  }

  componentDidMount() {
    client.onopen = () => {
      console.log("Websocket Client Connected");
    };
    client.onmessage = (message) => {
      console.log(message.data);
      const dataFromServer = JSON.parse(message.data);
      this.setState({
        board: dataFromServer.board,
        player: dataFromServer.player,
      });
    };
    client.onclose = () => {
      console.log("Websocket client disconnected");
    };
  }

  SendMove(cord) {
    console.log(cord);
    if (
      IsTurn(this.state.board, this.state.player) &&
      IsWinner(this.state.board) == 0 &&
      (cord.column === 0 || cord.column === 6)
    ) {
      const data = {
        row: cord.row,
        side: cord.column === 0 ? "Left" : "Right",
        player: this.state.player,
      };
      console.log(data);
      client.send(JSON.stringify(data));
    } else {
      console.log("Not your turn");
    }
  }

  render() {
    if (!this.state.board) {
      console.log("board is null");
      return <h1>waiting to connect</h1>;
    }
    const isWinner = IsWinner(this.state.board);

    if (IsTurn(this.state.board, this.state.player)) {
    }

    let text;
    if (isWinner === this.state.player) {
      text = "You won!!";
    } else if (isWinner === 3) {
      text = "Tie. Play again?";
    } else if (isWinner !== 0) {
      text = "You lose. Play again?";
    }
    return (
      <div>
        <Player
          isTurn={IsTurn(this.state.board, 1)}
          isPlayer1={true}
          areYouThisPlayer={1 === this.state.player}
        />
        <Board
          board={this.state.board}
          player={this.state.player}
          SendMove={this.SendMove}
        />
        <Player
          isTurn={IsTurn(this.state.board, 2)}
          isPlayer1={false}
          areYouThisPlayer={2 === this.state.player}
        />
        {
          // TODO: Turn this into A POPUP!!
          // TODO: <p class="message"> {text} </p>
        }
      </div>
    );
  }
}

export default App;
