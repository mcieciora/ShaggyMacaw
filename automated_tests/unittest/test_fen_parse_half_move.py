from pytest import mark, raises

from src.fen import Fen, NotIntegerHalfMoveValue


@mark.unittest
def test__unittest__fen__parse_half_move():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 2 1"
    test_object = Fen(original_fen)
    actual_data = test_object.parse_half_move("2")
    assert actual_data == 2, f"Expected: 2, actual: {actual_data}"


@mark.unittest
def test__unittest__fen__parse_half_move__not_integer():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - x 1"
    test_object = Fen(original_fen)
    with raises(NotIntegerHalfMoveValue):
        test_object.parse_half_move("x")
