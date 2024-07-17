from connect4.bot import bot_move, get_valid_locations
from connect4.game_logic import create_board, drop_piece

def test_get_valid_locations():
    board = create_board(6, 7)
    valid_locations = get_valid_locations(board)
    assert valid_locations == list(range(7))

def test_bot_move():
    board = create_board(6, 7)
    # Simulate player moves
    drop_piece(board, 0, 0, 1)
    drop_piece(board, 1, 0, 1)
    drop_piece(board, 2, 0, 1)
    # Bot should block player from winning
    assert bot_move(board, 4) == 0

    # Simulate bot winning move
    board = create_board(6, 7)
    drop_piece(board, 0, 0, 2)
    drop_piece(board, 1, 0, 2)
    drop_piece(board, 2, 0, 2)
    assert bot_move(board, 4) == 0
