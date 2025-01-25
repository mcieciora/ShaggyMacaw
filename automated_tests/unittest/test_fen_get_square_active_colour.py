from pytest import mark, raises

from src.fen import Fen, NoSquareInBoard, SquareEmpty


@mark.unittest
def test__unittest__fen__get_square_active_colour__is_white():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 2"
    test_object = Fen(original_fen)
    actual_data = test_object.get_square_active_colour("a1")
    assert actual_data is True, f"Expected: True, actual: {actual_data}"


@mark.unittest
def test__unittest__fen__get_square_active_colour__is_black():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 2"
    test_object = Fen(original_fen)
    actual_data = test_object.get_square_active_colour("a8")
    assert actual_data is False, f"Expected: False, actual: {actual_data}"


@mark.unittest
def test__unittest__fen__get_square_active_colour__is_empty():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 2"
    test_object = Fen(original_fen)
    with raises(SquareEmpty):
        test_object.get_square_active_colour("a3")


@mark.unittest
def test__unittest__fen__get_square_active_colour__no_square():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 2"
    test_object = Fen(original_fen)
    with raises(NoSquareInBoard):
        test_object.get_square_active_colour("xX")
