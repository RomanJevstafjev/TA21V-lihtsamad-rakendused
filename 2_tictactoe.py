gameField = [['.', '.', '.'],
             ['.', '.', '.'],
             ['.', '.', '.']]

def main():
    while True:
        print("---------------------------")

        drawField()

        print('---- First player move ----')
        while True:
            moveIsSuccess: bool = player_move('X')

            if moveIsSuccess:
                if checkWin():
                    print("Player win!")
                    break

                break
            else:
                print("Inccorect range, try one more time")

        drawField()

        print('---- Second player move ----')

        while True:
            moveIsSuccess: bool = player_move('O')
            
            if moveIsSuccess:
                if checkWin():
                    print("Player win!")
                    break
                break
            else:
                print("Inccorect range, try one more time")

        drawField()

def player_move(symbol):
    str_playerRow: str = input("Player, enter row:")
    playerRow: int = int(str_playerRow)
    str_playerCage: str = input("Player, enter cage:")
    playerCage: int = int(str_playerCage)

    cage: chr = gameField[playerRow - 1][playerCage - 1]

    if cage == '.':
        gameField[playerRow - 1][playerCage - 1] = symbol
        return True
    else:
        return False

def checkWin():



def drawField():
    for row in range(0, len(gameField)):
        rowResult: str = ""

        for cage in range(0, len(gameField[row])):
            rowResult = rowResult + gameField[row][cage]
        
        print(rowResult)

main()
