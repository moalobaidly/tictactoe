board = [0,1,2,3,4,5,6,7,8]
def printboard():
    print(f"  |   |   ")
    print(f"{board[0]} | {board[1]} | {board[2]} ")
    print("----------")
    print(f"{board[3]} | {board[4]} | {board[5]} ")
    print("----------")
    print(f"{board[6]} | {board[7]} | {board[8]} ")
    print(f"  |   |   ")
    x = int(input("Pick a number:"))
    changeboard(x)


def changeboard(number):
    character = input("Are you x or o?")
    board[number] = character
    print (board[number])
    checkwin()
    printboard()

def checkwin():
    if board[0] == board[1] == board [2]:
        print (f"the winner is {board [0]}")
        exit(1)
    elif board[3] == board[4] == board [5]:
        print (f"the winner is {board [3]}")
        exit(1)
    elif board[6] == board[7] == board [8]:
        print (f"the winner is {board [6]}")
        exit(1)
    elif board[0] == board[3] == board [6]:
        print (f"the winner is {board [0]}")
        exit(1)
    elif board[1] == board[4] == board [7]:
        print (f"the winner is {board [1]}")
        exit(1)
    elif board[2] == board[5] == board [8]:
        print (f"the winner is {board [2]}")
        exit(1)
    elif board[0] == board[4] == board [8]:
        print (f"the winner is {board [0]}")
        exit(1)
    elif board[2] == board[4] == board [6]:
        print (f"the winner is {board [6]}")
        exit(1)

def main():
    print("welcome to tic tac toe")
    printboard()


if __name__ == "__main__":
    main()