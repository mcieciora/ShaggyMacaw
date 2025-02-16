from pytest import mark

from src.fen import Fen
from src.move import Move


@mark.unittest
def test__unittest__move__update_clocks__promotion():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 2 1"
    test_object = Fen(original_fen)
    move = Move(original_square="d7", target_square="c8", is_promotion=True, promotion_piece="Q")
    test_object.update_clocks(move)
    actual_half_move_value = test_object.half_move_clock
    actual_full_move_value = test_object.full_move_number
    assert actual_half_move_value == 0, f"Expected: 0, actual: {actual_half_move_value}"
    assert actual_full_move_value == 1, f"Expected: 1, actual: {actual_full_move_value}"


@mark.unittest
def test__unittest__move__update_clocks__capture():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 2 1"
    test_object = Fen(original_fen)
    move = Move(original_square="c4", target_square="c6", is_capture=True)
    test_object.update_clocks(move)
    actual_half_move_value = test_object.half_move_clock
    actual_full_move_value = test_object.full_move_number
    assert actual_half_move_value == 0, f"Expected: 0, actual: {actual_half_move_value}"
    assert actual_full_move_value == 1, f"Expected: 1, actual: {actual_full_move_value}"


@mark.unittest
def test__unittest__move__update_clocks__en_passant():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 2 1"
    test_object = Fen(original_fen)
    move = Move(original_square="b4", target_square="a3", is_en_passant=True)
    test_object.update_clocks(move)
    actual_half_move_value = test_object.half_move_clock
    actual_full_move_value = test_object.full_move_number
    assert actual_half_move_value == 0, f"Expected: 0, actual: {actual_half_move_value}"
    assert actual_full_move_value == 1, f"Expected: 1, actual: {actual_full_move_value}"


@mark.unittest
def test__unittest__move__update_clocks__move_from_starting_position():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 2 1"
    test_object = Fen(original_fen)
    move = Move(original_square="d2", target_square="d4", is_move_legal=True)
    test_object.update_clocks(move)
    actual_half_move_value = test_object.half_move_clock
    actual_full_move_value = test_object.full_move_number
    assert actual_half_move_value == 2, f"Expected: 2, actual: {actual_half_move_value}"
    assert actual_full_move_value == 1, f"Expected: 1, actual: {actual_full_move_value}"


@mark.unittest
def test__unittest__move__update_clocks__move():
    original_fen = "4r1k1/1p3pp1/2b5/3Bn3/3p1NPp/7P/PP2P3/5R1K w - - 1 34"
    test_object = Fen(original_fen)
    move = Move(original_square="d2", target_square="d4", is_move_legal=True)
    test_object.update_clocks(move)
    actual_half_move_value = test_object.half_move_clock
    actual_full_move_value = test_object.full_move_number
    assert actual_half_move_value == 2, f"Expected: 2, actual: {actual_half_move_value}"
    assert actual_full_move_value == 34, f"Expected: 34, actual: {actual_full_move_value}"


@mark.unittest
def test__unittest__move__update_clocks__move_with_full_move_increase():
    original_fen = "4r1k1/1p3pp1/2b5/3Bn3/3p1NPp/7P/PP2P3/5R1K b - - 1 34"
    test_object = Fen(original_fen)
    move = Move(original_square="d2", target_square="d4", is_move_legal=True)
    test_object.update_clocks(move)
    actual_half_move_value = test_object.half_move_clock
    actual_full_move_value = test_object.full_move_number
    assert actual_half_move_value == 2, f"Expected: 2, actual: {actual_half_move_value}"
    assert actual_full_move_value == 35, f"Expected: 35, actual: {actual_full_move_value}"
