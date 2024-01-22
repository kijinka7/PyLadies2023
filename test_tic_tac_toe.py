import tic_tac_toe
import pytest

# Test EVALUATE 1
def test_evaluate_game_state():
    x_board = tic_tac_toe.evaluate("------xxx-----------")
    o_board = tic_tac_toe.evaluate("-----o--xoxx-----ooo")
    full_board = tic_tac_toe.evaluate("oxoxoxooxoxxoxooxxoo")
    space_left_board = tic_tac_toe.evaluate("oo-oxoxoxoxoxoxoxoxo")
    assert x_board == "x"
    assert o_board == "o"
    assert full_board == "!"
    assert space_left_board == "-"

# Test EVALUATE 2
# I added an exception to my original tic tac toe game, because I wanted to try how negative tests can work and also to practise exceptions...
def test_evaluate_board_length():
    with pytest.raises(ValueError):
        tic_tac_toe.evaluate("----x-----o-----")

# Test EVALUATE 3
def test_evaluate_board_input():
    with pytest.raises(ValueError):
        tic_tac_toe.evaluate("xy--------x--------o")

# Test EVALUATE 4
def test_evaluate_double_win():
    with pytest.raises(ValueError):
        tic_tac_toe.evaluate("xxxx----ooo---------")

# Test EVALUATE 5 
def test_evaluate_empty_board():
    empty_board = tic_tac_toe.evaluate("--------------------")
    assert empty_board == "-"

# Test MOVE 1
def test_move_correctly_marked_movement():
    new_board_pc = tic_tac_toe.move("----x---------------", "o", 0)
    new_board_player = tic_tac_toe.move("----x---------------", "x", 19)
    assert new_board_pc == "o---x---------------"
    assert new_board_player == "----x--------------x" 

# Test MOVE 2
def test_move_correct_mark_input():
    with pytest.raises(ValueError):
        tic_tac_toe.move("--------------------", "j", 6)
    
# What is a Python module and how does it differ from a Python package?
        # Python module is a file containing certain data like functions or variables. Package is more complex and contains several modules. But it can be imported similarily as a module.
# What are side effects and give some examples.
        # Side effects are changes caused by a function. For example when an imported module changes some variables or performs functions not specifically called.
# What are Exceptions and what to do if third-party code that we use throws them?
        # Exception is an error. We should try to catch them and adjust behaviour of our function.
# Using which keywords can you create, throw and catch your new custom Exception?
        # Custom exception is created by creating a new class wich inherits from the exception class, raise = throw, ewe catch exceptions by using try and catch
# Give examples of some benefits of testing?
        # Automated control of script, predicting and correcting errors. 
