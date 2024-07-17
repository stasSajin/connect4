import random
import numpy as np
from connect4.game_logic import is_valid_location, get_next_open_row, winning_move, drop_piece

def get_valid_locations(board: np.ndarray) -> list[int]:
    return [col for col in range(board.shape[1]) if is_valid_location(board, col)]

def bot_move(board: np.ndarray, connect: int) -> int:
    valid_locations = get_valid_locations(board)

    # Check if the AI can win in the next move
    for col in valid_locations:
        row = get_next_open_row(board, col)
        temp_board = board.copy()
        drop_piece(temp_board, row, col, 2)
        if winning_move(temp_board, 2, connect):
            return col

    # Check if the player can win in the next move and block them
    for col in valid_locations:
        row = get_next_open_row(board, col)
        temp_board = board.copy()
        drop_piece(temp_board, row, col, 1)
        if winning_move(temp_board, 1, connect):
            return col

    # Pick a random valid column
    return random.choice(valid_locations)
