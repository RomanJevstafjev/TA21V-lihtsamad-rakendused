import os

class Cell:
    def __init__(self, symbol):
        self.__symbol = symbol

    @property
    def symbol(self):
        return self.__symbol

class Position:
    def __init__(self, y_position, x_position):
        self.__y_position = y_position
        self.__x_position = x_position

    @property
    def y_position(self):
        return self.__y_position

    @y_position.setter
    def y_position(self, value: int):
        self.__y_position = value

    @property
    def x_position(self):
        return self.__x_position

    @x_position.setter
    def x_position(self, value: int):
        self.__x_position = value


class Player:
    def __init__(self, cell: Cell, position: Position):
        self.__cell = cell
        self.__position = position

    @property
    def cell(self):
        return self.__cell

    @property
    def position(self):
        return self.__position

    def move(self, free_positions: list[Position]):
        for i in range(0, len(free_positions)):
            print(f"{i + 1}. {free_positions[i].y_position + 1}, {free_positions[i].x_position + 1}")
        
        str_position_number: str = input(f"Choose position(1 - {len(free_positions)}):")
        position_number: int = int(str_position_number)

        if position_number <= 0 or position_number > len(free_positions):
            raise Exception("Incorrect position number.")

        self.__position.y_position = free_positions[position_number - 1].y_position
        self.__position.x_position = free_positions[position_number - 1].x_position

class Map:
    @property
    def map_height(self):
        return self.__map_height

    @property
    def map_width(self):
        return self.__map_width

    def set_map(self, wall_symbol: chr, cells_symbols: list[chr]):
        self.__wall_symbol = wall_symbol

        cells_width: int = len(cells_symbols[0])

        self.__cells = []
        for i in range(0, len(cells_symbols)):
            self.__cells.append([])

            for j in range(0, len(cells_symbols[i])):
                if cells_width != len(cells_symbols[i]):
                    raise Exception("All map lines must be the same width.")

                self.__cells[i].append(Cell(cells_symbols[i][j]))

        self.__map_height = len(self.__cells)
        self.__map_width = cells_width
    
    def draw(self):
        print(' ', end=' ')

        for i in range(0, self.__map_width):
            print(i + 1, end=' ')

        print()

        for i in range(0, self.__map_height):
            print(i + 1, end=' ')

            for j in range(0, self.__map_width):
                print(self.__cells[i][j].symbol, end=' ')

            print()

    def __reset_player_position(self, player_cell):
        for i in range(self.__map_height):
            for j in range(self.__map_width):
                if self.__cells[i][j].symbol == player_cell.symbol:
                    self.__cells[i][j] = Cell(' ')

    def set_player_position(self, player: Player):
        if self.__cells[player.position.y_position][player.position.x_position].symbol == self.__wall_symbol:
            raise Exception("This cell is visit.")

        self.__reset_player_position(player.cell)

        self.__cells[player.position.y_position][player.position.x_position] = player.cell

    def get_free_positions(self, position: Position):
        free_positions: list[Position] = []

        for i in range(position.y_position - 1, position.y_position + 2):
            if i < 0 or i > self.__map_height - 1:
                continue

            for j in range(position.x_position - 1, position.x_position + 2):
                if j < 0 or j > self.__map_width - 1 or self.__cells[i][j].symbol == self.__wall_symbol or position.y_position == i and position.x_position == j:
                    continue
                
                free_position: Position = Position(i, j)
                free_positions.append(free_position)

        return free_positions

class GameStatus:
    @staticmethod
    def check_win(player: Player, win_position: Position):
        if player.position.y_position == win_position.y_position and player.position.x_position == win_position.x_position:
            return True

        return False

def main():
    map_cells: list[list[chr]] = [
        [' ', '#', ' ', '#', ' '],
        [' ', '#', ' ', '#', ' '],
        [' ', '#', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', '#'],
        ['#', '#', ' ', ' ', '!'],
    ]

    map: Map = Map()
    map.set_map('#', map_cells)

    player: Player = Player(Cell('X'), Position(0, 0))
    win_position: Position = Position(4, 4)

    map.set_player_position(player)

    while True:
        map.draw()

        free_positions: list[Position] = map.get_free_positions(player.position)

        try:
            player.move(free_positions)
        except:
            print("Incorrect value. Try one more time.")
            input()

            continue
        finally:
            os.system("cls")

        map.set_player_position(player)

        player_is_win: bool = GameStatus.check_win(player, win_position)
        if player_is_win:
            print("You win!")
            break

main()