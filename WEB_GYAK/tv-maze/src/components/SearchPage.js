import React from "react";
import SearchForm from "./SearchForm";
import SearchTileset from "./SearchTileSet";

class SearchPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      serchTerm: "",
    };
  }

  render() {
    return (
      <div>
        <div className="row">
          <SearchForm
            onSubmit={(text) => this.setState({ searchTerm: text })}
          />{" "}
        </div>{" "}
        <div className="row mt-2"> </div>{" "}
      </div>
    );
  }
}

export default SearchPage;
