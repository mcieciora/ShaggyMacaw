from pytest import mark

from src.fen import Fen
from src.move import Move


@mark.unittest
def test__unittest__fen__update_en_passant__single_pawn_move():
    original_fen = "r1bqkbnr/pp1ppppp/2n5/8/3pP3/5N2/PPP2PPP/RNBQKB1R w KQkq - 0 4"
    test_object = Fen(original_fen)
    move = Move(original_square="a2", target_square="a3", piece_value="P")
    test_object.update_en_passant(move, (0, 2), 1)
    actual_data = test_object.available_en_passant
    assert actual_data == "-", f"Expected: -, actual: {actual_data}"


@mark.unittest
def test__unittest__fen__update_en_passant__double_pawn_move():
    original_fen = "r1bqkbnr/pp1ppppp/2n5/8/3pP3/5N2/PPP2PPP/RNBQKB1R w KQkq - 0 4"
    test_object = Fen(original_fen)
    move = Move(original_square="a2", target_square="a4", piece_value="P")
    test_object.update_en_passant(move, (0, 3), 1)
    actual_data = test_object.available_en_passant
    assert actual_data == "a3", f"Expected: a3, actual: {actual_data}"


@mark.unittest
def test__unittest__fen__update_en_passant__non_pawn_move():
    original_fen = "r1bqkbnr/pp1ppppp/2n5/8/3pP3/5N2/PPP2PPP/RNBQKB1R w KQkq - 0 4"
    test_object = Fen(original_fen)
    move = Move(original_square="c1", target_square="e3", piece_value="B")
    test_object.update_en_passant(move, (2, 3), 1)
    actual_data = test_object.available_en_passant
    assert actual_data == "-", f"Expected: -, actual: {actual_data}"
