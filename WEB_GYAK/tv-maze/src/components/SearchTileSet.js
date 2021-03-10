import React from 'react';

class SearchTileSet extends React.Component {
        constructor(props) {
            super(props);
            this.state = {
                shows: []
            }
        }
        async getShows(searchTerm) {
            if (searchTerm !== null) {
                const response = await fetch('http://api.tvmaze.com/search/shows?q=${searchTerm}');
                const res = await response.json();
                this.setState({
                    shows: res.map(showObject => showObject.show)
                });
            }

        }
        componentDidMount() {
            this.getShows(this.props.searchTerm)

        }
        componentDidUpdate() {
            if (this.props.searchTerm !== prewProp.searchTerm) {
                this.getShows(this.props.searchTerm);
            }
        }


        render() {
            const shows = this.state.shows;
            const tiles = show.map(
                show => ( < SearchTile show = { show }
                    key = { show.id }
                    />)
                );
                return ( <div className = "col-12">
                            <div className = "row" >
                            <div className = "col-12" >
                                <h1 > Találatok </h1> </div>
                    </div> 
                    <div className = "row" >
                        <div className = "col-12" >
                            <h1>Találatok </h1>
                        </div>
                    </div>
                        
                );
            }
            }
        


        export default SearchTileSet;