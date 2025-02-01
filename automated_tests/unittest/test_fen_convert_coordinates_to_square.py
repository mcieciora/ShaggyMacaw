from pytest import mark

from src.fen import Fen


@mark.unittest
def test__unittest__fen__convert_coordinates_to_square():
    original_fen = "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23"
    test_object = Fen(original_fen)
    actual_data = test_object.convert_coordinates_to_square(0, 2)
    assert actual_data == "a3", f"Expected: gxf6, actual: {actual_data}"
