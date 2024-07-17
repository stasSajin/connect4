import numpy as np
from connect4.game_logic import create_board, drop_piece, is_valid_location, get_next_open_row, winning_move

def test_create_board():
    board = create_board(6, 7)
    assert board.shape == (6, 7)
    assert np.all(board == 0)

def test_drop_piece():
    board = create_board(6, 7)
    drop_piece(board, 0, 0, 1)
    assert board[0][0] == 1

def test_is_valid_location():
    board = create_board(6, 7)
    assert is_valid_location(board, 0)
    drop_piece(board, 5, 0, 1)
    assert is_valid_location(board, 0) == False, "Column is full"
    drop_piece(board, 4, 0, 1)
    drop_piece(board, 3, 0, 1)
    drop_piece(board, 2, 0, 1)
    drop_piece(board, 1, 0, 1)
    drop_piece(board, 0, 0, 1)
    assert not is_valid_location(board, 0), "Column is full"

# test_is_valid_location()s

def test_get_next_open_row():
    board = create_board(6, 7)
    assert get_next_open_row(board, 0) == 0
    drop_piece(board, 0, 0, 1)
    assert get_next_open_row(board, 0) == 1

def test_winning_move():
    board = create_board(6, 7)
    # Test horizontal win
    for col in range(4):
        drop_piece(board, 0, col, 1)
    assert winning_move(board, 1, 4) is True

    board = create_board(6, 7)
    # Test vertical win
    for row in range(4):
        drop_piece(board, row, 0, 1)
    assert winning_move(board, 1, 4) is True

    board = create_board(6, 7)
    # Test positively sloped diagonal win
    for i in range(4):
        drop_piece(board, i, i, 1)
    assert winning_move(board, 1, 4) is True

    board = create_board(6, 7)
    # Test negatively sloped diagonal win
    for i in range(4):
        drop_piece(board, 3-i, i, 1)
    assert winning_move(board, 1, 4) is True