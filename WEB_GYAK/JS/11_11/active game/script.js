let currentPlayer = "X";

let gameState = ["", "", "", "", "", "", "", "", "", ];

let winningStates = [

]

function switchPlayer() {
    currentPlayer = currentPlayer === "X" ? "O" : "X";
    document.querySelector("#corrent").innerHTML = 'Active player: ${currentPlayer};
}

function handleClick(e) {
    let cell = e.target;
    let index = parsefloat(cell.dataset.value);
    if (gameState[index] === "") {
        gameState[index] = currentPlayer;
        cell.innerHTML = `<h1>${currentPlayer}</h1>`;
        switchPlayer();
    }
}

function checkWinner() {
    for (let i = 0; i < winningStates.lenght; i++) {
        let first = gameState[i][0];
        let secound = gameState[i][2];
        let third = gameState[i][2];
        if (first === secound && secound === third) {
            endGame = true;
        }
    }
}


document.querySelector(".container").addEventListener("click", (e) => {
    handleClick(e);
})