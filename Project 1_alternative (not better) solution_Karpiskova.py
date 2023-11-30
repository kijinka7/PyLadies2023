from random import randrange

def choice():
    player_choice = int(input("Where do you want to place a cross? Enter a number of an empty spot on the board (from 1-20): "))
    while player_choice > 20 or player_choice < 1:
        player_choice = int(input("Wrong input, you must enter a number of an empty field on the board (from 1-20): "))
    player_choice = player_choice - 1
    return player_choice

def moves(player_choice, computer_choice, board):
    if player_choice == 0 and computer_choice == 0:
        board = "x" + board[player_choice+1:]
        board = "o" + board[computer_choice+1:]
        return board
    elif player_choice == 0:
        board = "x" + board[player_choice+1:]
        board = board[:computer_choice] + "o" + board[computer_choice+1:]
        return board
    elif computer_choice == 0:
        board = board[:player_choice] + "x" + board[player_choice+1:]
        board = "o" + board[computer_choice+1:]
        return board
    else:
        board = board[:player_choice] + "x" + board[player_choice+1:]
        board = board[:computer_choice] + "o" + board[computer_choice+1:]
        return board

def evaluate(player_choice, computer_choice, board):
    if "-" in board:
        while board[player_choice] != "-":
            print("Choose a different location to place your mark.")
            player_choice = choice()
        while board[computer_choice] != "-" or computer_choice == player_choice:
            computer_choice = randrange(0,20)
        print(f"Computer places its mark on space {computer_choice + 1} of the game board.")
        board = moves(player_choice, computer_choice, board)
        return player_choice, computer_choice, board
    else:
        print("There are no more moves you can make. It's a draw. Play again.")
        board = "--------------------"
        return player_choice, computer_choice, board



print("Welcome to 1-D Tic-Tac-Toe game.")
board = "--------------------"
print(f"This is your game board, each space on the board has a number from 1-20, if you manage to place 3 crosses next to each other you win!\n{board}")
while "xxx" not in board or "ooo" not in board:
    player_choice = choice()
    computer_choice = randrange(0,20)
    player_choice, computer_choice, board = evaluate(player_choice, computer_choice, board)
    print(f"The new status of the game board is:\n{board}")
    if "xxx" in board:
        print("You win!")
        break

    elif "ooo" in board:
        print("Sorry, the computer wins!")
        break