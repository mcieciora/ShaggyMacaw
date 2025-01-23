from pytest import mark

from src.chess_board import ChessBoard


@mark.unittest
def test__unittest__chess_board__is_pawn_in_starting_position__white_starting_position():
    original_fen = "4k3/P7/8/8/R7/7r/6p1/6K1 b - - 0 1"
    test_object = ChessBoard(original_fen)
    actual_data = test_object.is_pawn_in_starting_position("p", 1)
    assert actual_data is True, f"Expected: True, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__is_pawn_in_starting_position__black_starting_position():
    original_fen = "4k3/P7/8/8/R7/7r/6p1/6K1 b - - 0 1"
    test_object = ChessBoard(original_fen)
    actual_data = test_object.is_pawn_in_starting_position("P", 6)
    assert actual_data is True, f"Expected: True, actual: {actual_data}"

@mark.unittest
def test__unittest__chess_board__is_pawn_in_starting_position__not_in_starting_position():
    original_fen = "4k3/8/8/8/R7/6pr/8/6K1 w - - 0 1"
    test_object = ChessBoard(original_fen)
    actual_data = test_object.is_pawn_in_starting_position("P", 5)
    assert actual_data is False, f"Expected: False, actual: {actual_data}"
