from pytest import mark

from src.chess_board import ChessBoard


@mark.unittest
def test__unittest__chess_board__is_pawn_next_move_promotion__white_promotion():
    original_fen = "4k3/P7/8/8/R7/7r/6p1/6K1 b - - 0 1"
    test_object = ChessBoard(original_fen)
    actual_data = test_object.is_pawn_next_move_promotion("P", 1)
    assert actual_data is True, f"Expected: True, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__is_pawn_next_move_promotion__black_promotion():
    original_fen = "4k3/P7/8/8/R7/7r/6p1/6K1 b - - 0 1"
    test_object = ChessBoard(original_fen)
    actual_data = test_object.is_pawn_next_move_promotion("p", 6)
    assert actual_data is True, f"Expected: True, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__is_pawn_next_move_promotion__no_promotion_available():
    original_fen = "4k3/8/8/8/R7/6pr/8/6K1 w - - 0 1"
    test_object = ChessBoard(original_fen)
    actual_data = test_object.is_pawn_next_move_promotion("p", 5)
    assert actual_data is False, f"Expected: False, actual: {actual_data}"
