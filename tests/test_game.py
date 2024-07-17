import pytest
from connect4.game import get_player_name, draw_board
import streamlit as st
from connect4.game_logic import create_board

def test_get_player_name():
    assert get_player_name(0) == '🔴 Player 1'
    assert get_player_name(1) == '🟡 AI Bot'
    assert get_player_name(2) == '🔴 Player 1'

@pytest.fixture
def setup_streamlit_session_state():
    st.session_state.board = create_board(6, 7)
    st.session_state.turn = 0
    st.session_state.game_over = False
    st.session_state.rows = 6
    st.session_state.cols = 7
    st.session_state.connect = 4
    yield
    st.session_state.clear()

def test_draw_board(setup_streamlit_session_state):
    board = st.session_state.board
    draw_board(board)
    assert True  # No easy way to assert Streamlit UI, but we ensure it runs without error
