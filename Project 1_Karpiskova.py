from random import randrange

def evaluate(board):
    if "xxx" in board:
        return "x"
    elif "ooo" in board:
        return "o"
    elif "-" not in board:
        return "!"
    else:
        return "-"

def move(board, mark, position):
    if mark == "x":
        board = board[:position] + "x" + board[position+1:]
        return board
    else:
        board = board[:position] + "o" + board[position+1:]
        return board

def player_move(board):
    position = int(input("Where do you want to place a cross? Enter a number of an empty spot on the board (from 0-19): "))
    while position > 19 or position < 0 or board[position] != "-":
        position = int(input("Wrong input, you must enter a number of an empty field on the board (from 0-19): "))
    board = move(board, "x", position)
    return board

def pc_move(board):
    position = randrange(0,20)
    while board[position] != "-":
        position = randrange(0,20)
    board = move(board, "o", position)
    return board

def tictactoe():
    board = "--------------------"
    while evaluate(board) == "-":
        board = player_move(board)
        print(board)
        if evaluate(board) == "-":
            board = pc_move(board)
            print(board)
        else:
            break
    
    if evaluate(board) == "x":
        print("You win!")
    elif evaluate(board) == "o":
        print("PC wins!")
    else:
        print("No more space left, it's a draw!")
    
tictactoe()