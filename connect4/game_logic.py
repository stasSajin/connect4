import numpy as np

def create_board(rows: int, cols: int) -> np.ndarray:
    return np.zeros((rows, cols))

def drop_piece(board: np.ndarray, row: int, col: int, piece: int) -> None:
    board[row][col] = piece

def is_valid_location(board: np.ndarray, col: int) -> bool:
    return board[-1][col] == 0

def get_next_open_row(board: np.ndarray, col: int) -> int:
    for r in range(len(board)):
        if board[r][col] == 0:
            return r
    return -1

def winning_move(board: np.ndarray, piece: int, connect: int) -> bool:
    rows, cols = board.shape
    # Check horizontal locations
    for c in range(cols - connect + 1):
        for r in range(rows):
            if all(board[r][c+i] == piece for i in range(connect)):
                for i in range(connect):
                    board[r][c+i] = piece + 2
                return True

    # Check vertical locations
    for c in range(cols):
        for r in range(rows - connect + 1):
            if all(board[r+i][c] == piece for i in range(connect)):
                for i in range(connect):
                    board[r+i][c] = piece + 2
                return True

    # Check positively sloped diagonals
    for c in range(cols - connect + 1):
        for r in range(rows - connect + 1):
            if all(board[r+i][c+i] == piece for i in range(connect)):
                for i in range(connect):
                    board[r+i][c+i] = piece + 2
                return True

    # Check negatively sloped diagonals
    for c in range(cols - connect + 1):
        for r in range(connect - 1, rows):
            if all(board[r-i][c+i] == piece for i in range(connect)):
                for i in range(connect):
                    board[r-i][c+i] = piece + 2
                return True

    return False
