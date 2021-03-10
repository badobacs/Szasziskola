import React from 'react';

class SearchTile extends React.Component{

    render(){
        const show=this.props.show;
        const rating = show.rating.avarage;
        const ratingLabel = rating !== null ? rating + '/10' : 'unkrown';
        return(
            <div className="film">
                <div className="titel"></div>
                <img src={show.image !== null : show.image.medium : ''} />
                <div className="rating">{ratingLabel}</div>

                </div>
            </div>
        );
        
    }
}

export default SearchTile;