from pytest import mark

from src.fen import Fen
from src.move import Move
from src.piece import PieceType


@mark.unittest
def test__unittest__fen__update_board_setup__promotion():
    original_fen = "5k2/PR3p2/3N2p1/8/3p2Pp/2n2K1P/4r3/8 b - - 1 42"
    test_object = Fen(original_fen)
    move = Move(original_square="a7", target_square="a8", is_promotion=True, promotion_piece="Q")
    test_object.update_board_setup(move, original=(0, 6), target=(0, 7))

    actual_data = test_object.board_setup[7][0]
    assert actual_data.piece_type is PieceType.QUEEN, f"Expected: {PieceType.QUEEN}, actual: {actual_data.piece_type}"

    actual_data = test_object.board_setup[6][0]
    assert actual_data is PieceType.EMPTY, f"Expected: {PieceType.EMPTY}, actual: {actual_data}"


@mark.unittest
def test__unittest__fen__update_board_setup__castling():
    original_fen = "r1bqkb1r/pp3ppp/2n2n2/2pp4/3P4/2N2NP1/PP2PPBP/R1BQK2R b KQkq - 2 7"
    test_object = Fen(original_fen)
    move = Move(original_square="e1", target_square="g1", is_castling=True)
    test_object.update_board_setup(move, original=(4, 0), target=(6, 0))

    actual_data = test_object.board_setup[0][6]
    assert actual_data.piece_type is PieceType.KING, f"Expected: {PieceType.KING}, actual: {actual_data.piece_type}"

    actual_data = test_object.board_setup[0][4]
    assert actual_data is PieceType.EMPTY, f"Expected: {PieceType.EMPTY}, actual: {actual_data}"


@mark.unittest
def test__unittest__fen__update_board_setup__en_passant():
    original_fen = "r3r1k1/pp3p1p/1bn5/5Pp1/3p1Nb1/6P1/PP1NP1BP/R1R2K2 w - g6 0 18"
    test_object = Fen(original_fen)
    move = Move(original_square="f5", target_square="g6", is_en_passant=True)
    test_object.update_board_setup(move, original=(5, 4), target=(6, 5))

    actual_data = test_object.board_setup[5][6]
    assert actual_data.piece_type is PieceType.PAWN, f"Expected: {PieceType.PAWN}, actual: {actual_data.piece_type}"
    assert actual_data.active_colour_white, f"Expected: True, actual: {actual_data.active_colour_white}"

    actual_data = test_object.board_setup[4][5]
    assert actual_data is PieceType.EMPTY, f"Expected: {PieceType.EMPTY}, actual: {actual_data}"

    actual_data = test_object.board_setup[5][5]
    assert actual_data is PieceType.EMPTY, f"Expected: {PieceType.EMPTY}, actual: {actual_data}"


@mark.unittest
def test__unittest__fen__update_board_setup__move():
    original_fen = "3k4/1p1r4/pR6/8/4K3/1P6/8/8 w - - 5 51"
    test_object = Fen(original_fen)
    move = Move(original_square="e4", target_square="d5")
    test_object.update_board_setup(move, original=(4, 3), target=(3, 5))

    actual_data = test_object.board_setup[5][3]
    assert actual_data.piece_type is PieceType.KING, f"Expected: {PieceType.KING}, actual: {actual_data.piece_type}"

    actual_data = test_object.board_setup[3][4]
    assert actual_data is PieceType.EMPTY, f"Expected: {PieceType.EMPTY}, actual: {actual_data}"


@mark.unittest
def test__unittest__fen__update_board_setup__take():
    original_fen = "3k4/1p6/pR1r4/8/4K3/1P6/8/8 w - - 5 51"
    test_object = Fen(original_fen)
    move = Move(original_square="b6", target_square="d6")
    test_object.update_board_setup(move, original=(1, 5), target=(3, 5))

    actual_data = test_object.board_setup[5][3]
    assert actual_data.piece_type is PieceType.ROOK, f"Expected: {PieceType.ROOK}, actual: {actual_data.piece_type}"

    actual_data = test_object.board_setup[5][1]
    assert actual_data is PieceType.EMPTY, f"Expected: {PieceType.EMPTY}, actual: {actual_data}"
