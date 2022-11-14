import React from "react";
import Piece from "./Piece";

class Column extends React.Component {
  constructor() {
    super();
    this.state = {
      hovering: false,
    };
    this.OnMouseExitHandler = this.OnMouseExitHandler.bind(this);
    this.OnMouseOverHandler = this.OnMouseOverHandler.bind(this);
  }

  OnMouseOverHandler() {
    this.setState({
      hovering: true,
    });
  }

  OnMouseExitHandler() {
    this.setState({
      hovering: false,
    });
  }

  render() {
    let valueCopy = this.props.value.slice();
    if (this.state.hovering && this.props.isTurn) {
      const indexOfEmptyPiece = valueCopy.lastIndexOf(0);
      if (indexOfEmptyPiece !== -1) {
        valueCopy[indexOfEmptyPiece] = this.props.player === 1 ? 3 : 4;
      }
    }

    var key = 0;
    const pieces = valueCopy.map((item) => {
      key += 1;
      return <Piece key={key} value={item} />;
    });
    return (
      <div
        data-testid="column"
        className="column"
        onMouseOver={() => this.OnMouseOverHandler()}
        onMouseOut={() => this.OnMouseExitHandler()}
        onClick={() => this.props.clickHandler(this.props.colNum)}
      >
        {pieces}
      </div>
    );
  }
}

export default Column;
