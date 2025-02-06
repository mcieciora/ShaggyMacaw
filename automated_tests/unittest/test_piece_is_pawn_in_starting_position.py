from pytest import mark

from src.piece import Pawn


@mark.unittest
def test__unittest__piece__is_pawn_in_starting_position__white_starting_position():
    test_object = Pawn("P", (0, 1))
    actual_data = test_object.is_pawn_in_starting_position()
    assert actual_data is True, f"Expected: True, actual: {actual_data}"


@mark.unittest
def test__unittest__piece__is_pawn_in_starting_position__black_starting_position():
    test_object = Pawn("p", (0, 6))
    actual_data = test_object.is_pawn_in_starting_position()
    assert actual_data is True, f"Expected: True, actual: {actual_data}"


@mark.unittest
def test__unittest__piece__is_pawn_in_starting_position__not_in_starting_position():
    test_object = Pawn("P", (0, 6))
    actual_data = test_object.is_pawn_in_starting_position()
    assert actual_data is False, f"Expected: False, actual: {actual_data}"
