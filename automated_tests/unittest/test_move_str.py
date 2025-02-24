from pytest import mark

from src.move import Move


@mark.unittest
def test__unittest__move__str__move():
    test_data = Move(original_square="d2", target_square="d4")
    actual_value = str(test_data)
    assert actual_value == "d2d4", f"Expected: d2d4, actual: {actual_value}"


@mark.unittest
def test__unittest__move__str__promotion():
    test_data = Move(original_square="d7", target_square="d8", is_promotion=True, promotion_piece="Q")
    actual_value = str(test_data)
    assert actual_value == "d8=Q", f"Expected: d8=Q, actual: {actual_value}"


@mark.unittest
def test__unittest__move__str__promotion_with_capture():
    test_data = Move(original_square="d7", target_square="c8", is_promotion=True, promotion_piece="Q", is_capture=True)
    actual_value = str(test_data)
    assert actual_value == "d7c8=Q", f"Expected: d7c8=Q, actual: {actual_value}"
