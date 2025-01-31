from pytest import mark

from src.chess_board import ChessBoard


@mark.unittest
def test__unittest__chess_board__generate_rook_moves__one_rook():
    original_fen = "4qk2/2r3bp/1p1pb1p1/p4r2/1nPPpn2/2NB3P/5NP1/R1BQK2R w KQ - 2 9"
    expected_data = ["Ra2", "Ra3", "Ra4", "Rxa5", "Rb1"]
    test_object = ChessBoard(original_fen)
    actual_data = test_object.generate_rook_moves(0, "R")
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"

    expected_data = ["Rh2", "Rg1", "Rf1"]
    actual_data = test_object.generate_rook_moves(7, "R")
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__generate_rook_moves__two_rooks():
    original_fen = "4qk2/2r3bp/1p1pb1p1/p4r2/1nPPpn2/2NB3P/5NP1/R1BQK2R w KQ - 2 9"
    expected_data = ["Rg5", "Rh5", "Rf6", "Rff7", "Re5", "Rd5", "Rfc5", "Rb5"]
    test_object = ChessBoard(original_fen)
    actual_data = test_object.generate_rook_moves(37, "r")
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"

    expected_data = ["Rc8", "Rb7", "Ra7", "Rc6", "Rcc5", "Rxc4", "Rd7", "Re7", "Rcf7"]
    actual_data = test_object.generate_rook_moves(50, "r")
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"
