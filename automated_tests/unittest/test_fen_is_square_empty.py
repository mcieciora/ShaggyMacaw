from pytest import mark, raises

from src.fen import Fen, NoSquareInBoard


@mark.unittest
def test__unittest__fen__is_square_empty__is_empty():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 2"
    test_object = Fen(original_fen)
    actual_data = test_object.is_square_empty("a3")
    assert actual_data is True, f"Expected: True, actual: {actual_data}"


@mark.unittest
def test__unittest__fen__is_square_empty__is_not_empty():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 2"
    test_object = Fen(original_fen)
    actual_data = test_object.is_square_empty("a1")
    assert actual_data is False, f"Expected: False, actual: {actual_data}"


@mark.unittest
def test__unittest__fen__is_square_empty__not_integer():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 2"
    test_object = Fen(original_fen)
    with raises(NoSquareInBoard):
        test_object.is_square_empty("xX")
