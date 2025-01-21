from pytest import mark, raises

from src.fen import Fen, NotIntegerFullMoveValue


@mark.unittest
def test__unittest__fen__parse_full_move():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 2"
    test_object = Fen(original_fen)
    actual_data = test_object.parse_full_move("2")
    assert actual_data == 2, f"Expected: 2, actual: {actual_data}"


@mark.unittest
def test__unittest__fen__parse_full_move__not_integer():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 x"
    test_object = Fen(original_fen)
    with raises(NotIntegerFullMoveValue):
        test_object.parse_full_move("x")
