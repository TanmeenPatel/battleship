from ship import Ship

def create_board() -> list[list[Ship | None]]:
    '''
    Create a 2D list representing the game board. The size will be
    5x5 with all slots set to None.
    '''
    board = [
        [None] * 5,
        [None] * 5,
        [None] * 5,
        [None] * 5,
        [None] * 5
    ]
    return board

def print_board(board: list[list[Ship | None]]) -> None:
    '''
    Prints the game board with the ships.
    You can assume the board is 5x5.
    '''
    print("-" * 7)
    i = 0
    while i < 5:
        print('|', end='')
        j = 0
        while j < 5:
            if isinstance(board[i][j], Ship) and board[i][j].has_sunk():
                symbol = 'X'
            elif isinstance(board[i][j], Ship):
                symbol = board[i][j].get_name()[-1]
            else:
                symbol = ' '
            print(symbol, end='')
            j += 1
        print('|')
        i += 1
    print("-" * 7)


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


def main():
    '''Runs the game.'''
    # 1. Create the list of ships
    ships = Ship.create_ships()

    # 2. Create the 5x5 board
    board = create_board()

    # 3. Place your ships in the board based on their coordinates
    i = 0
    while i < len(ships):
        ship = ships[i]
        x, y = ship.get_coord()
        board[y][x] = ship
        i += 1

    # 4. Continuously prompt the user for input until all ships are sunk.
    #    Whenever a ship is sunk, update the ship's status accordingly.
    print()
    print("Game started. Fire at will!")
    attempts = 0
    while attempts < 10:
        user_input = input(f"Enter X, Y coordinate [{attempts+1}/10]: ")
        # fetch the inputs
        tokens = user_input.split(', ')
        x = int(tokens[0])
        y = int(tokens[1])
        # check if the coordinates are valid
        if x < 0 or x >= 5 or y < 0 or y >= 5:
            # go back to the input
            print('Invalid coordinates. Try again.')
            attempts += 1
            continue
         
        # we reach here if valid coordinates are given
        ship = board[y][x]
        if not isinstance(ship, Ship):
            print('Miss!')
            attempts += 1
            continue

        # we reach here if it is a ship
        if ship.has_sunk():
            print('Miss!')
        else:
            ship.got_hit()
            print(f'You sank {ship.get_name()}!')
            print_board(board)

        if is_finished(board):
            print()
            print("Congratulations! All ships are sunk.")
            return

        attempts += 1

    # if we reach here, it means we exited the loop, meaning we've used all attempts
    print('Game over after 10 attempts! Try again next time!')


if __name__ == "__main__":
    main()