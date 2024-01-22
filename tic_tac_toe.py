# I added some exceptions and other stuff to my original script - in the "evaluate" and "move" functions to practise testing.
from random import randrange

# I googled the code with "all" below since you encouraged googling in our last lesson :D I understand that what I am working with is a "set" similar to dictionary but includes only "keys" without values.
def specific_character_in_string(string):
    valid_characters = {"x", "-", "o"}
    return all(character in valid_characters for character in string)

def check_board_validity(board):
    if len(board) != 20:
        raise ValueError("The board does not have the required length.")
    elif not specific_character_in_string(board):
        raise ValueError("The board uses invalid characters.")
    elif ("xxx" in board and "ooo" in board) or "xxxx" in board or "oooo" in board:
        raise ValueError("The board already contained a winning set of marks, the last moves were invalid.")

def evaluate(board):
    check_board_validity(board)
    if "xxx" in board:
        return "x"  
    elif "ooo" in board:
        return "o"
    elif "-" not in board:
        return "!"
    else:
        return "-"

def move(board, mark, position):
    if mark != "x" and mark != "o":
        raise ValueError("Invalid mark input.")
    elif mark == "x":
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

if __name__ == "__main__":
    tictactoe()