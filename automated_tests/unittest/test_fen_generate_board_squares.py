from pytest import mark

from src.fen import Fen


@mark.unittest
def test__fen__generate_board_squares():
    """Cover tc-0"""
    test_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    test_data = Fen(test_fen)
    unique_squares = list(set(test_data.board_squares))
    board_length = len(unique_squares)
    assert board_length == 64, f"Board length for fen: {test_fen} is {board_length}, expected: 64"
