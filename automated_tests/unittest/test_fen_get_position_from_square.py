from pytest import mark, raises

from src.fen import Fen, NoSquareInBoard


@mark.unittest
def test__unittest__fen__get_position_from_square():
    test_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    test_data = Fen(test_fen)
    actual_value = test_data.get_position_from_square("a1")
    assert actual_value == (0, 0), f"Expected: a1, actual: {test_data.board_squares[0]}"
    actual_value = test_data.get_position_from_square("e5")
    assert actual_value == (4, 4), f"Expected: a1, actual: {test_data.board_squares[0]}"


@mark.unittest
def test__unittest__fen__get_position_from_square__no_square_in_board():
    test_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    test_data = Fen(test_fen)
    with raises(NoSquareInBoard):
        actual_value = test_data.get_position_from_square("x1")
