const search = async (queryString) => {
    let response = await fetch(`http://api.tvmaze.com/search/shows?q=${queryString}`)
                .then(response => response.json() );
    console.log(response);
    return response;
}

const createMovieTile = (show) => {
    return `
        <div>
            <img src=${show.image !== null ? show.image.medium : "#"}>
            <h4>${show.name}</h4>
            <h5>Értékelés: ${show.rating.avarage !== null ? show.rating.avarage 
                : "nincs adat"}</h5>
        </div> 
    `
}

document.querySelector("#b").addEventListener("click", async () => {
    let queryString = document.querySelector("#s").value;
    let responseArray = await search (queryString);
    let resultHTML = "";

    responseArray.forEach((value) => {
        resultHTML += createMovieTile(value.show);
    });
     document.querySelector(".results").innerHTML = resultHTML;
});



//console.log(response.body);