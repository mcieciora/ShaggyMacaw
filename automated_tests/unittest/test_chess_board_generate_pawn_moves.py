from pytest import mark

from src.chess_board import ChessBoard


@mark.unittest
def test__unittest__chess_board__generate_pawn_moves__single_push():
    original_fen = "r1b3k1/1p2P1p1/2nq1p2/pPN3P1/r1Rp3p/3Nb2P/P1Q1PBP1/5RK1 w - - 4 23"
    expected_data = ["a3"]
    test_object = ChessBoard(original_fen)
    actual_data = test_object.generate_pawn_moves(8, "P")
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__generate_pawn_moves__blocked_single_push():
    original_fen = "r1b3k1/1p2P1p1/2nq1p2/pPN3P1/r1Rp3p/3Nb2P/P1Q1PBP1/5RK1 w - - 4 23"
    expected_data = []
    test_object = ChessBoard(original_fen)
    actual_data = test_object.generate_pawn_moves(23, "P")
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__generate_pawn_moves__double_push():
    original_fen = "r1b3k1/1p2P1p1/2nq1p2/pPN3P1/r1Rp3p/3Nb2P/P1Q1PBP1/5RK1 w - - 4 23"
    expected_data = ["g3", "g4"]
    test_object = ChessBoard(original_fen)
    actual_data = test_object.generate_pawn_moves(14, "P")
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__generate_pawn_moves__no_double_push_over_another_piece():
    original_fen = "r1b3k1/1p2P1p1/2nq1p2/pPN3P1/r1Rp3p/3Nb2P/P1Q1PBP1/5RK1 w - - 4 23"
    expected_data = []
    test_object = ChessBoard(original_fen)
    actual_data = test_object.generate_pawn_moves(12, "P")
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__generate_pawn_moves__capture():
    original_fen = "r1b3k1/1p2P1p1/2nq1p2/pPN3P1/r1Rp3p/3Nb2P/P1Q1PBP1/5RK1 w - - 4 23"
    expected_data = ["g6", "gxf6"]
    test_object = ChessBoard(original_fen)
    actual_data = test_object.generate_pawn_moves(38, "P")
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__generate_pawn_moves__en_passant():
    original_fen = "r1b3k1/1p2P1p1/2nq1p2/pPN3P1/r1Rp3p/3Nb2P/P1Q1PBP1/5RK1 w - a6 4 23"
    expected_data = ["b6", "bxa6", "bxc6"]
    test_object = ChessBoard(original_fen)
    actual_data = test_object.generate_pawn_moves(33, "P")
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__generate_pawn_moves__promotion():
    original_fen = "r1b3k1/1p2P1p1/2nq1p2/pPN3P1/r1Rp3p/3Nb2P/P1Q1PBP1/5RK1 w - - 4 23"
    expected_data = ["e8=Q", "e8=R", "e8=N", "e8=B"]
    test_object = ChessBoard(original_fen)
    actual_data = test_object.generate_pawn_moves(52, "P")
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__generate_pawn_moves__promotion_with_capture():
    original_fen = "2br2k1/1p2P1p1/2nq1p2/pPN3P1/r1Rp3p/3Nb2P/P1Q1PBP1/5RK1 w - - 4 23"
    expected_data = ["e8=Q", "e8=R", "e8=N", "e8=B", "exd8=Q", "exd8=R", "exd8=N", "exd8=B"]
    test_object = ChessBoard(original_fen)
    actual_data = test_object.generate_pawn_moves(52, "P")
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__generate_pawn_moves__blocked_promotion():
    original_fen = "2b1r1k1/1p2P1p1/2nq1p2/pPN3P1/r1Rp3p/3Nb2P/P1Q1PBP1/5RK1 w - - 4 23"
    expected_data = []
    test_object = ChessBoard(original_fen)
    actual_data = test_object.generate_pawn_moves(52, "P")
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"
