from pytest import mark, raises

from src.fen import Fen, NotIntegerFullMoveValue


@mark.unittest
def test__fen__parse_full_move():
    """Cover tc-0"""
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    test_object = Fen(original_fen)
    test_data = test_object.parse_full_move(2)
    assert test_data == 2, f"Expected: 2, actual: {test_data}"


@mark.unittest
def test__fen__parse_full_move__not_integer():
    """Cover tc-0"""
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    test_object = Fen(original_fen)
    with raises(NotIntegerFullMoveValue):
        test_object.parse_full_move("x")
