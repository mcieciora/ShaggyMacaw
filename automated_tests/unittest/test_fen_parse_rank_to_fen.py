from pytest import mark

from src.fen import Fen


@mark.unittest
def test__unittest__fen__parse_rank_to_fen():
    original_fen = "r1bqkbnr/pp1ppppp/2n5/8/3pP3/5N2/PPP2PPP/RNBQKB1R w KQkq - 0 4"
    test_object = Fen(original_fen)
    test_data = {
        0: "RNBQKB1R",
        1: "PPP2PPP",
        2: "5N2",
        3: "3pP3",
        4: "8",
        5: "2n5",
        6: "pp1ppppp",
        7: "r1bqkbnr"
    }
    for test_index, expected_value in test_data.items():
        actual_data = test_object.parse_rank_to_fen(test_object.board_setup[test_index])
        assert actual_data == expected_value, f"Expected: {expected_value}, actual: {actual_data}"
