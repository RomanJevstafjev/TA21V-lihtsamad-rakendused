from weakref import WeakMethod


class Cell:
    def __init__(self, symbol):
        self.symbol = symbol

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, value):
        if value != ' ' and value != '#' and value != 'X':
            raise ValueError("Cell can be only ' ' or '#'.")
        
        self.__symbol = value

class Player:
    def __init__(self, player_cell: Cell, x_position: int, y_position: int):
        self.__cell = player_cell
        self.__x_position = x_position
        self.__y_position = y_position
    
    @property
    def cell(self):
        return self.__cell

    @property
    def x_position(self):
        return self.__x_position

    @property
    def y_position(self):
        return self.__y_position
    
    def move(self):
        while True:
            direction: str = input("Up/Down/Right/Left:")

            if direction == "Up":
                self.__y_position -= 1
            elif direction == "Down":
                self.__y_position += 1
            elif direction == "Right":
                self.__x_position += 1
            elif direction == "Left":
                self.__x_position -= 1
            else:
                continue

            break

class Map:
    __cells = []

    def upload_map(self, cells_symbols, player):
        for i in range(len(cells_symbols)):
            self.__cells.append([])

            for j in range(len(cells_symbols[i])):
                self.__cells[i].append(Cell(cells_symbols[i][j]))

        self.set_player_position(player)
    
    def draw(self):
        for i in range(0, len(self.__cells)):
            for j in range(0, len(self.__cells[i])):
                print(self.__cells[i][j].symbol, end='')

            print()

    def __reset_player_position(self, player_cell):
        for i in range(0, len(self.__cells)):
            for j in range(0, len(self.__cells[i])):
                if self.__cells[i][j].symbol == player_cell.symbol:
                    self.__cells[i][j].symbol = ' '

    def set_player_position(self, player: Player):
        self.__reset_player_position(player.cell)

        self.__cells[player.y_position][player.x_position] = player.cell

def main():
    map_cells = [
        [' ', '#', ' ', '#', ' '],
        [' ', '#', ' ', '#', ' '],
        [' ', '#', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', '#'],
        ['#', '#', ' ', ' ', ' '],
    ]

    player: Player = Player(Cell('X'), 0, 0)

    map: Map = Map()
    map.upload_map(map_cells, player)

    while True:
        map.draw()

        player.move()
        map.set_player_position(player)

main()