import React from 'react';

class SearchPage extends React.Component{

    constructor(props){
        super(props);
        this.state={
            text:''
        }
    }

    render(){
        return(
            <div className="col-12" id="searchForm">
                <form>
                    <div className="form-row align-item-center">
                        <div className="col-auto">
                            <input
                            type="text"
                            id="sorozat-cim"
                            className="form-control"
                            name="title"
                            placeholder="Sorozat cime"
                            value={this.state.text}
                            onChange={event => this.inputChange(event)}/>
                            <input
                            type="button"
                            id="kereses"
                            value="Kereses"
                            className="btn"></input>
                        </div>
                    </div>
                </form>
            </div>




        );
    }
}


export default Searchform;