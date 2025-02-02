from pytest import mark

from src.piece import Pawn


@mark.unittest
def test__unittest__piece__is_pawn_next_move_promotion__white_promotion():
    test_object = Pawn("P", (0, 6))
    actual_data = test_object.is_pawn_next_move_promotion()
    assert actual_data is True, f"Expected: True, actual: {actual_data}"


@mark.unittest
def test__unittest__piece__is_pawn_next_move_promotion__black_promotion():
    test_object = Pawn("p", (0, 1))
    actual_data = test_object.is_pawn_next_move_promotion()
    assert actual_data is True, f"Expected: True, actual: {actual_data}"


@mark.unittest
def test__unittest__piece__is_pawn_next_move_promotion__no_promotion_available():
    test_object = Pawn("p", (0, 5))
    actual_data = test_object.is_pawn_next_move_promotion()
    assert actual_data is False, f"Expected: False, actual: {actual_data}"
