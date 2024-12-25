console.log('hi')
msg = document.getElementById('message')
const gameBoard = document.getElementById('game-board')

document.getElementById('start-game').addEventListener("click", () => {
    fetch('/start-game', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            msg.innerText = data.message;
            createboard()
            console.log(data.board)
        });
    document.getElementById('start-game').disabled = true;
})

document.getElementById('restart-game').addEventListener('click', () => {
    document.getElementById('start-game').disabled = false;
    gameBoard.innerHTML = ''
    msg.innerText = ''
})

function createboard() {
    gameBoard.innerHTML = ''
    for (let i = 0; i < 5; i++) {
        const rowDiv = document.createElement('div')
        for (let j = 0; j < 5; j++) {
            const cellDiv = document.createElement('button')
            cellDiv.classList.add('cell')
            cellDiv.addEventListener("click", () => {
                fetch('/move', {
                    method: 'POST', 
                    headers: { 'Content-Type': 'application/json'}, 
                    body: JSON.stringify({x: i, y: j})})
                .then(response => response.json())
                .then(data => {
                    if (!data.hit) {
                        cellDiv.classList.add('miss')
                    }
                    else if (data.hit) {
                        cellDiv.classList.add('hit')
                        cellDiv.innerText = '🚢'
                    }
                    msg.innerText = data.message + data.attempts;
                })
                cellDiv.disabled = true
            })
            rowDiv.appendChild(cellDiv)
        }
        gameBoard.append(rowDiv)
    }
}