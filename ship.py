class Ship:
    def __init__(self, x: int, y: int, name: str) -> None:
        '''
        Initialize a ship object with given coordinates and name.

        There are 4 attributes of the the ship:
        x (int): The x coordinate of the ship.
        y (int): The y coordinate of the ship.
        name (str): The name or type of the ship.
        sunk (bool): Indicates whether the ship has sunk.
        '''
        self.x = x
        self.y = y
        self.name = name
        self.sunk: bool = False


    def got_hit(self):
        '''
        Update the status of the ship when it gets hit.
        If the ship is hit, it is marked as sunk.
        '''
        self.sunk = True


    def has_sunk(self) -> bool:
        '''Get the status of the ship.'''
        return self.sunk


    def get_name(self) -> str:
        '''Get the name of the ship.'''
        return self.name


    def get_coord(self) -> tuple[int, int]:
        '''Get the coordinate of the ship.'''
        return self.x, self.y


    def __repr__(self) -> str:
        '''
        Returns a formatted string representation of the ship.

        The formatted string includes the ship's name followed by its status:
        - If the ship has sunk, the format is "{name}: Sunk".
        - If the ship hasn't sunk, the format is "{name}: Afloat".
        '''
        if self.sunk:
            return f'{self.name}: Sunk'
        else:
            return f'{self.name}: Afloat'

    
    # you will need to modify the implementation of this method
    def create_ships() -> list["Ship"]:
        '''
        This method will now ask for the user to create ships by asking for a symbol, x and y coordinate. 
        The symbol will be used for the ship's name. A correct input is in the format <symbol> <x> <y> 
        where 
            - symbol is a letter from A to J
            - x and y are valid coordinates that can fit the ship onto the board.
        
        A maximum of 3 ships can be made. If this maximum is reached, it will stop and return the ships made. 
        However, if the user has not hit the maximum but is finished, 
        the user can enter END SHIPS which will also stop and return the ships made.       
        '''
        print('Creating ships...')
        no_of_ships = 0
        ships = []
        while no_of_ships < 3:
            ship_details = input('> ')
            if ship_details == 'END SHIPS':
                break
            ship_details = ship_details.split(' ')

            # Checking if input is valid
            if ship_details[0] < 'A' or ship_details[0] > 'J':
                print('Error!')
                continue

            try:
                if int(ship_details[1]) < 0 or int(ship_details[1]) > 4:
                    print('Error!')
                    continue
                if int(ship_details[2]) < 0 or int(ship_details[2]) > 4:
                    print('Error!')
                    continue
            except ValueError:
                print('Error!')
                continue

            if ships:
                invalid_ship = False
                for ship in ships:
                    if (int(ship_details[1]), int(ship_details[2])) == ship.get_coord():
                        print('Error!')
                        invalid_ship = True
                    if (ship.name == ship_details[0]):
                        print('Error!')
                        invalid_ship = True
                if invalid_ship:
                    continue

            # Creating ship if ship is valid
            no_of_ships += 1
            ship_details[1] = int(ship_details[1])
            ship_details[2] = int(ship_details[2])

            ship = Ship(ship_details[1], ship_details[2], ship_details[0])
            ships += [ship]
            print(f'Success! {ship_details[0]} added at ({ship_details[1]}, {ship_details[2]})')

        return ships


if __name__ == '__main__':
    Ship.create_ships()