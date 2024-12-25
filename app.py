from flask import Flask, request, render_template, jsonify
from ship import Ship

attempts = 10

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/start-game", methods=['POST'])
def start_game():
    global board
    board = [
        [None] * 5,
        [None] * 5,
        [None] * 5,
        [None] * 5,
        [None] * 5
    ]
    ships = Ship.create_ships()
    global attempts
    attempts = 10

    i = 0
    while i < len(ships):
        ship = ships[i]
        x, y = ship.get_coord()
        board[y][x] = ship
        i += 1

    return jsonify({'message': 'Game started.'})

def is_finished(board: list[list[Ship | None]]):
    '''
    Check if all ships on the 2D list game board are sunk.
    Returns True if all ships are sunk, otherwise False.
    '''
    for y in board:
        for x in y:
            if isinstance(x, Ship):
                if x.has_sunk() == False:
                    return False
    return True

@app.route("/move", methods = ["POST"])
def move():
    global attempts
    if attempts == 0:
        return jsonify({'message':'You lost! Attempts over'})
    attempts -= 1 
    data = request.get_json()
    x = data.get('x')
    y = data.get('y')
    print(x, y)

    ship = board[x][y]
    if not isinstance(ship, Ship):
        return jsonify({'message': 'MISS!', 'attempts': attempts})

    if ship.has_sunk():
        return jsonify({'message': 'MISS!', 'attempts': attempts})
    else:
        ship.got_hit()
        print(f'You sank {ship.get_name()}!')
        if is_finished(board):
            return jsonify({'message': 'GAME OVER! You sank the last ship. Congrats!'})
        else:
            return jsonify({'message': f'You sank {ship.get_name()}!', 'attempts': attempts})