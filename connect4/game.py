import streamlit as st
import numpy as np
from connect4.game_logic import create_board, drop_piece, is_valid_location, get_next_open_row, winning_move
from connect4.bot import bot_move

# Initialize game state
if 'board' not in st.session_state:
    st.session_state.board = create_board(6, 7)
    st.session_state.turn = 0
    st.session_state.game_over = False
    st.session_state.rows = 6
    st.session_state.cols = 7
    st.session_state.connect = 4

# Sidebar configuration
st.sidebar.title('Game Configuration')
rows = st.sidebar.number_input('Number of rows', min_value=4, max_value=10, value=6)
cols = st.sidebar.number_input('Number of columns', min_value=4, max_value=10, value=7)
connect = st.sidebar.number_input('Number of continuous cells to win', min_value=3, max_value=10, value=4)

if st.sidebar.button('Start New Game'):
    st.session_state.board = create_board(rows, cols)
    st.session_state.turn = 0
    st.session_state.game_over = False
    st.session_state.rows = rows
    st.session_state.cols = cols
    st.session_state.connect = connect
    st.rerun()

# Display the game board
st.title('Connect Four')
st.write(f"""
### How to Play
- Player 1 (🔴) and the AI Bot (🟡) take turns dropping pieces into the columns of the game board.
- The goal is to be the first to form a horizontal, vertical, or diagonal line of `{st.session_state.connect}` of one's own pieces.
- Click on an empty cell to drop your piece in that column.
- The game will indicate when a player has won.
""")
board: np.ndarray = st.session_state.board

def get_player_name(turn: int) -> str:
    return '🔴 Player 1' if turn % 2 == 0 else '🟡 AI Bot'

def draw_board(board: np.ndarray) -> None:
    for row in range(st.session_state.rows):
        cols = st.columns(st.session_state.cols)
        for col in range(st.session_state.cols):
            if board[st.session_state.rows - 1 - row][col] == 0:
                if cols[col].button(' ', key=f'{row}-{col}'):
                    if not st.session_state.game_over:
                        if is_valid_location(board, col):
                            row = get_next_open_row(board, col)
                            piece = 1 if st.session_state.turn % 2 == 0 else 2
                            drop_piece(board, row, col, piece)
                            if winning_move(board, piece, st.session_state.connect):
                                st.session_state.game_over = True
                                st.session_state.winner = get_player_name(st.session_state.turn)
                            st.session_state.turn += 1
                            st.rerun()
            elif board[st.session_state.rows - 1 - row][col] == 1:
                cols[col].button('🔴', key=f'{row}-{col}', disabled=True)
            elif board[st.session_state.rows - 1 - row][col] == 2:
                cols[col].button('🟡', key=f'{row}-{col}', disabled=True)
            elif board[st.session_state.rows - 1 - row][col] == 3:
                cols[col].button('🔴', key=f'{row}-{col}', disabled=True)
            elif board[st.session_state.rows - 1 - row][col] == 4:
                cols[col].button('🟡', key=f'{row}-{col}', disabled=True)

draw_board(board)

if st.session_state.game_over:
    st.success(f'{st.session_state.winner} wins!')

if not st.session_state.game_over and st.session_state.turn % 2 == 1:
    col = bot_move(board, st.session_state.connect)
    if is_valid_location(board, col):
        row = get_next_open_row(board, col)
        piece = 2
        drop_piece(board, row, col, piece)
        if winning_move(board, piece, st.session_state.connect):
            st.session_state.game_over = True
            st.session_state.winner = '🟡 AI Bot'
        st.session_state.turn += 1
        st.rerun()

if st.button('Restart Game'):
    st.session_state.board = create_board(st.session_state.rows, st.session_state.cols)
    st.session_state.turn = 0
    st.session_state.game_over = False
    st.rerun()
