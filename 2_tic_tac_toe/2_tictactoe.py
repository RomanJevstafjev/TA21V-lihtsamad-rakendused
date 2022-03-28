from argparse import ArgumentError
import os

class Player:
    def __init__(self, cell):
        self.__cell = cell

    @property
    def player_cell(self):
        return self.__cell

    def request_cell(self):
        str_line_number: str = input(f"<{self.__cell.symbol}> Enter line number:")
        str_cell_number: str = input(f"<{self.__cell.symbol}> Enter cell number:")

        line_number: int = int(str_line_number)
        cell_number: int = int(str_cell_number)

        cell_response: CellResponse = CellResponse(line_number - 1, cell_number - 1)

        return cell_response

class CellResponse:
    def __init__(self, line_index: int, cell_index: int):
        self.__line_index = line_index
        self.__cell_index = cell_index

    @property
    def line_index(self):
        return self.__line_index
    
    @property
    def cell_index(self):
        return self.__cell_index

class Cell:
    def __init__(self, symbol: chr = '.'):
        self.__symbol = symbol
    
    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, value):
        if value == 'X' or value == 'O' or value == '.':
            self.__symbol = value
        else:
            raise ValueError("Value can be only X or Y.")

class Map:
    __map_size: int = 3
    __cells = None

    @property
    def cells(self):
        return self.__cells

    def generate_map(self):
        self.__cells = []
        
        for i in range(self.__map_size):
            self.__cells.append([])

            for j in range(self.__map_size):
                self.__cells[i].append(Cell())

    def change_cell(self, line_index: int, cell_index: int, player_cell: Cell):
        if self.__cells[line_index][cell_index].symbol != '.':
            raise ArgumentError()

        self.__cells[line_index][cell_index] = player_cell

    def draw(self):
        if self.__cells == None:
            raise Exception("Map is not generate.")
        
        for i in range(len(self.__cells)):
            for j in range(len(self.__cells[i])):
                print(self.__cells[i][j].symbol, end=' ')

            print()

class GameStatus:
    def check_win(self, map: Map, player: Player):
        player_symbol: chr = player.player_cell.symbol

        straights_is_confirm: bool = self.__check_straights(map.cells, player_symbol)
        diagonals_is_confirm: bool = self.__check_diagonals(map.cells, player_symbol)

        if straights_is_confirm or diagonals_is_confirm:
            return True

        return False
    
    def __check_straights(self, cells, symbol: chr):
        horizontal: int
        vertical: int

        for i in range(0, len(cells)):
            horizontal = 0
            vertical = 0
            
            for j in range(0, len(cells[i])):
                if cells[i][j].symbol == symbol:
                    horizontal += 1

                if cells[j][i].symbol == symbol:
                    vertical += 1

            if horizontal == 3 or vertical == 3:
                return True

        return False

    def __check_diagonals(self, cells, symbol: chr):
        left_diagonal: int = 0
        right_diagonal: int = 0

        for i in range(0, len(cells)):
            if cells[i][i].symbol == symbol:
                left_diagonal += 1

            if cells[i][2 - i].symbol == symbol:
                right_diagonal += 1

        if left_diagonal == 3 or right_diagonal == 3:
            return True

        return False

    def check_dead_heat(self, map: Map):
        for line in map.cells:
            for cell in line:
                if cell.symbol == '.':
                    return False

        return True

def main():
    map: Map = Map()
    map.generate_map()

    gameStatus: GameStatus = GameStatus()

    players = [
        Player(Cell('X')),
        Player(Cell('O'))
    ]

    current_player_index: int = 0
    while True:
        map.draw()

        try:
            cell_response: CellResponse = players[current_player_index].request_cell()
            map.change_cell(cell_response.line_index, cell_response.cell_index, players[current_player_index].player_cell)
        except:
            print("Incorrect value, please try one more time.")
            input()

            continue
        finally:
            os.system('cls')

        is_win: bool = gameStatus.check_win(map, players[current_player_index])
        if is_win:
            print(f"Player <{players[current_player_index].player_cell.symbol}> is win.")
            break

        is_dead_heat: bool = gameStatus.check_dead_heat(map)
        if is_dead_heat:
            print("Dead heat.")
            break

        if current_player_index != len(players) - 1:
            current_player_index += 1
        else:
            current_player_index = 0

main()
