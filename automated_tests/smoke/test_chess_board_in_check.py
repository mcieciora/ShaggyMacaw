from pytest import mark

from src.chess_board import ChessBoard


test_data_dict = {
    "test_resource_1": {
        "fen": "r4b1r/pp1k1ppp/8/8/8/2N3P1/PP2PP1P/R1B1K2R w KQ - 0 14",
        "object_field": "in_check",
        "expected_result": False
    },
    "test_resource_2": {
        "fen": "8/4kp2/6p1/5N2/3p2Pp/2n2K1P/P7/8 b - - 1 44",
        "object_field": "in_check",
        "expected_result": True
    },
    "test_resource_3": {
        "fen": "r2qkb1r/pp3ppp/8/1Q6/8/2N3P1/PP2PP1P/R1B1K2R b KQkq - 0 12",
        "object_field": "in_check",
        "expected_result": True
    }
}


def get_parametrized_test_set():
    parametrized_test_set_list = []
    for test_data in test_data_dict.values():
        parametrized_test_set_list.append(test_data)
    return parametrized_test_set_list


@mark.smoke
@mark.parametrize("test_data", get_parametrized_test_set(), ids=test_data_dict.keys())
def test__smoke__chess_board__in_check(test_data):
    test_object = ChessBoard(test_data["fen"])
    test_object.generate_all_possible_moves()
    actual_data = test_object.in_check
    expected_data = getattr(test_object, test_data["object_field"])
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"
