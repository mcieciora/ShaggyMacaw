from pytest import mark

from src.chess_board import ChessBoard

test_data_dict = {
    "test_resource_1": {
        "fen": "5k2/1R3p2/6p1/4N3/6Pp/2n2K1P/P2pr3/N7 b - - 1 42",
        "index": 12,
        "piece": "r",
        "expected_result": ["Rg1", "Rhe1", "Rf1#", "Rd1", "Rc1", "Rb1", "Rxa1", "Rhh2", "Rxh3+"]
    },
    "test_resource_2": {
        "fen": "5k2/1R3p2/6p1/4N3/6Pp/2n2K1P/P2pr3/N6r b - - 1 42",
        "index": 7,
        "piece": "r",
        "expected_result": ["Re1", "Rf2+", "Rg2", "Rh2", "Re3+", "Re4", "Rxe5"]
    },
    "test_resource_3": {
        "fen": "5k2/1R3p2/6p1/4N3/6Pp/2n2K1P/P2pr3/N6r b - - 1 42",
        "index": 12,
        "piece": "r",
        "expected_result": ["Ree1", "Rf2+", "Rg2", "Reh2", "Re3+", "Re4", "Rxe5"]
    }
}


def get_parametrized_test_set():
    parametrized_test_set_list = []
    for test_key, test_data in test_data_dict.items():
        parametrized_test_set_list.append((test_key, test_data, test_data["expected_result"]))
    return parametrized_test_set_list


@mark.smoke
@mark.parametrize("test_key,test_data,expected_output", get_parametrized_test_set(), ids=test_data_dict.keys())
def test__smoke__chess_board__generate_pawn_moves(test_key, test_data, expected_output):
    test_object = ChessBoard(test_data["fen"])
    actual_result = test_object.generate_rook_moves(test_data["index"], test_data["piece"])
    assert actual_result == test_data["expected_result"], (f"Failed on {test_key}, expected: "
                                                           f"{test_data['expected_result']}, actual: "
                                                           f"{actual_result}")
