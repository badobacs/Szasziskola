function activate(a) {
    let div = e.target;
    // let id=div.ad;
    // document.querySelector(`#`)
    div.style.background = "red"

    let divs = document.querySelectorAll(".cell");
    console.log(divs);
    for (let i = 0; i < 4; i++) {
        if (divs[i].id != id) {
            document.querySelector(`#${divs[i].id}`).style.background = "white";
        }
    }
}




document.querySelector("#first").addEventListener("click", (e) => { activate(e) });
document.querySelector("#secound").addEventListener("click", (e) => { activate(e) });
document.querySelector("#third").addEventListener("click", (e) => { activate(e) });
document.querySelector("#fourth").addEventListener("click", (e) => { activate(e) });