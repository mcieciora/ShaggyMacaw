from pytest import mark

from src.chess_board import ChessBoard


@mark.unittest
def test__unittest__chess_board__in_check__no_check():
    original_fen = "2b1r1k1/1p3pp1/2n5/2N5/Q2p1NPp/7P/PP2P1B1/2q2RK1 b - - 2 28"
    test_object = ChessBoard(original_fen)
    test_object.generate_all_possible_moves()
    actual_data = test_object.in_check
    assert actual_data is False, f"Expected: False, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__in_check__check():
    original_fen = "1r1q1rk1/Q2npp1p/6p1/2P2b2/8/4BN2/PbP2PPP/2KR1B1R w - - 0 13"
    test_object = ChessBoard(original_fen)
    test_object.generate_all_possible_moves()
    actual_data = test_object.in_check
    assert actual_data is True, f"Expected: True, actual: {actual_data}"
