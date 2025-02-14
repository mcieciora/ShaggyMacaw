from pytest import mark

from src.chess_board import ChessBoard
from src.piece import Move


@mark.unittest
def test__unittest__evaluation__move_piece__single_push():
    expected_data = "rnbqkbnr/pppppppp/8/8/8/3P4/PPP1PPPP/RNBQKBNR b KQkq - 0 1"
    test_object = ChessBoard("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    move = Move(original_square="d2", target_square="d3", is_move_legal=True)
    test_object.move_piece(move)
    actual_data = test_object.fen.regenerate_fen()
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__evaluation__move_piece__double_push():
    expected_data = "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq d3 0 1"
    test_object = ChessBoard("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    move = Move(original_square="d2", target_square="d4", is_move_legal=True)
    test_object.move_piece(move)
    actual_data = test_object.fen.regenerate_fen()
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__evaluation__move_piece__knight_move():
    expected_data = "rnbqkbnr/ppp1pppp/8/3p4/3P4/2N5/PPP1PPPP/R1BQKBNR b KQkq - 1 2"
    test_object = ChessBoard("rnbqkbnr/ppp1pppp/8/3p4/3P4/8/PPP1PPPP/RNBQKBNR w KQkq d6 0 2")
    move = Move(original_square="b1", target_square="c3", is_move_legal=True)
    test_object.move_piece(move)
    actual_data = test_object.fen.regenerate_fen()
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__evaluation__move_piece__knight_capture():
    expected_data = "rn1qkbnr/ppp1pppp/4b3/3N4/3P4/8/PPP1PPPP/R1BQKBNR b KQkq - 0 3"
    test_object = ChessBoard("rn1qkbnr/ppp1pppp/4b3/3p4/3P4/2N5/PPP1PPPP/R1BQKBNR w KQkq - 2 3")
    move = Move(original_square="c3", target_square="d5", is_move_legal=True, is_capture=True)
    test_object.move_piece(move)
    actual_data = test_object.fen.regenerate_fen()
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__evaluation__move_piece__bishop_move():
    expected_data = "rn1qkbnr/ppp1pppp/4b3/3p4/3P4/2N5/PPP1PPPP/R1BQKBNR w KQkq - 2 3"
    test_object = ChessBoard("rnbqkbnr/ppp1pppp/8/3p4/3P4/2N5/PPP1PPPP/R1BQKBNR b KQkq - 1 2")
    move = Move(original_square="c8", target_square="e6", is_move_legal=True)
    test_object.move_piece(move)
    actual_data = test_object.fen.regenerate_fen()
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__evaluation__move_piece__bishop_capture():
    expected_data = "rn1qkbnr/ppp1pppp/8/3b4/3P4/8/PPP1PPPP/R1BQKBNR w KQkq - 0 4"
    test_object = ChessBoard("rn1qkbnr/ppp1pppp/4b3/3N4/3P4/8/PPP1PPPP/R1BQKBNR b KQkq - 0 3")
    move = Move(original_square="e6", target_square="d5", is_move_legal=True, is_capture=True)
    test_object.move_piece(move)
    actual_data = test_object.fen.regenerate_fen()
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__evaluation__move_piece__rook_move():
    expected_data = "3rk1nr/ppp4p/2nqpp2/3b2p1/Q2P4/2P2N2/PP2PPPP/R3KB1R w KQk - 2 11"
    test_object = ChessBoard("r3k1nr/ppp4p/2nqpp2/3b2p1/Q2P4/2P2N2/PP2PPPP/R3KB1R b KQkq - 1 10")
    move = Move(original_square="a8", target_square="d8", is_move_legal=True)
    test_object.move_piece(move)
    actual_data = test_object.fen.regenerate_fen()
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__evaluation__move_piece__rook_capture():
    expected_data = "3R2nr/ppp4p/2k2p2/4q1p1/8/2P1PP2/PP3P1P/4KB1R b K - 0 16"
    test_object = ChessBoard("3r2nr/ppp4p/2k2p2/4q1p1/8/2P1PP2/PP3P1P/3RKB1R w K - 0 16")
    move = Move(original_square="d1", target_square="d8", is_move_legal=True, is_capture=True)
    test_object.move_piece(move)
    actual_data = test_object.fen.regenerate_fen()
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__evaluation__move_piece__queen_move():
    expected_data = "r3k1nr/ppp4p/2nqpp2/3b2p1/Q2P4/2P2N2/PP2PPPP/R3KB1R b KQkq - 1 10"
    test_object = ChessBoard("r3k1nr/ppp4p/2nqpp2/3b2p1/3P4/2P2N2/PP2PPPP/R2QKB1R w KQkq - 0 10")
    move = Move(original_square="d1", target_square="a5", is_move_legal=True)
    test_object.move_piece(move)
    actual_data = test_object.fen.regenerate_fen()
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__evaluation__move_piece__queen_capture():
    expected_data = "r3k1nr/ppp4p/2nqpp2/3b2p1/3P4/2P2N2/PP2PPPP/R2QKB1R w KQkq - 0 10"
    test_object = ChessBoard("r2qk1nr/ppp4p/2nBpp2/3b2p1/3P4/2P2N2/PP2PPPP/R2QKB1R b KQkq - 0 9")
    move = Move(original_square="d8", target_square="d6", is_move_legal=True, is_capture=True)
    test_object.move_piece(move)
    actual_data = test_object.fen.regenerate_fen()
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__evaluation__move_piece__king_move():
    expected_data = "3r2nr/pppk3p/2nqpp2/3b2p1/Q2P4/2P2N2/PP2PPPP/3RKB1R w K - 4 12"
    test_object = ChessBoard("3rk1nr/ppp4p/2nqpp2/3b2p1/Q2P4/2P2N2/PP2PPPP/3RKB1R b Kk - 3 11")
    move = Move(original_square="e8", target_square="d7", is_move_legal=True)
    test_object.move_piece(move)
    actual_data = test_object.fen.regenerate_fen()
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__evaluation__move_piece__king_capture():
    expected_data = "3r2nr/ppp4p/2kqpp2/3b2p1/3P4/2P2N2/PP2PPPP/3RKB1R w K - 0 13"
    test_object = ChessBoard("3r2nr/pppk3p/2Qqpp2/3b2p1/3P4/2P2N2/PP2PPPP/3RKB1R b K - 0 12")
    move = Move(original_square="d7", target_square="c6", is_move_legal=True, is_capture=True)
    test_object.move_piece(move)
    actual_data = test_object.fen.regenerate_fen()
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__evaluation__move_piece__capture():
    expected_data = "rnbq1rk1/ppppppbp/6p1/8/2BPn3/2N5/PPP1NPPP/R1BQK2R w KQ - 0 6"
    test_object = ChessBoard("rnbq1rk1/ppppppbp/5np1/8/2BPP3/2N5/PPP1NPPP/R1BQK2R b KQ - 4 5")
    move = Move(original_square="f6", target_square="e4", is_move_legal=True, is_capture=True)
    test_object.move_piece(move)
    actual_data = test_object.fen.regenerate_fen()
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__evaluation__move_piece__en_passant():
    expected_data = "rnbq2k1/ppp2r1p/6p1/4p3/4N3/2p2N2/PP3PPP/R1BQ1RK1 w - - 0 12"
    test_object = ChessBoard("rnbq2k1/ppp2r1p/6p1/4p3/2PpN3/5N2/PP3PPP/R1BQ1RK1 b - c3 0 11")
    move = Move(original_square="d4", target_square="c3", is_move_legal=True,  is_en_passant=True)
    test_object.move_piece(move)
    actual_data = test_object.fen.regenerate_fen()
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__evaluation__move_piece__pawn_promotion():
    expected_data = "rnbq2k1/ppp2r1p/6p1/4p3/4N3/5N1P/P1Q2PP1/RqB2RK1 w - - 0 14"
    test_object = ChessBoard("rnbq2k1/ppp2r1p/6p1/4p3/4N3/5N1P/PpQ2PP1/R1B2RK1 b - - 0 13")
    move = Move(original_square="b2", target_square="b1", is_move_legal=True, is_promotion=True, promotion_piece="Q")
    test_object.move_piece(move)
    actual_data = test_object.fen.regenerate_fen()
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__evaluation__move_piece__pawn_promotion_with_capture():
    expected_data = "rnbq2k1/ppp2r1p/6p1/4p3/4N3/5N1P/P1Q2PP1/q1B2RK1 w - - 0 14"
    test_object = ChessBoard("rnbq2k1/ppp2r1p/6p1/4p3/4N3/5N1P/PpQ2PP1/R1B2RK1 b - - 0 13")
    move = Move(original_square="b2", target_square="a1", is_move_legal=True, is_promotion=True, is_capture=True,
                promotion_piece="Q")
    test_object.move_piece(move)
    actual_data = test_object.fen.regenerate_fen()
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__evaluation__move_piece__castling():
    expected_data = "rnbq2k1/ppp2r1p/6p1/3pp3/4N3/5N2/PPP2PPP/R1BQ1RK1 b - - 1 10"
    test_object = ChessBoard("rnbq2k1/ppp2r1p/6p1/3pp3/4N3/5N2/PPP2PPP/R1BQK2R w KQ d6 0 10")
    move = Move(original_square="e1", target_square="g1", is_move_legal=True, is_castling=True)
    test_object.move_piece(move)
    actual_data = test_object.fen.regenerate_fen()
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"
