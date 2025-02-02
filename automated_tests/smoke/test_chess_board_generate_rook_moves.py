from pytest import mark

from src.chess_board import ChessBoard
from src.piece import Piece

test_data_dict = {
    "test_resource_1": {
        "fen": "5k2/1R3p2/6p1/4N3/6Pp/2n2K1P/P2pr3/N7 b - - 1 42",
        "value": "r",
        "position": (4, 1),
        "expected_result": ["e2e3", "e2e4", "e2e5", "e2e1", "e2f2", "e2g2", "e2h2"]
    },
    "test_resource_2": {
        "fen": "5k2/1R3p2/6p1/4N3/6Pp/2n2K1P/P2pr3/N6r b - - 1 42",
        "value": "r",
        "position": (7, 0),
        "expected_result": ["h1h2", "h1h3", "h1g1", "h1f1", "h1e1", "h1d1", "h1c1", "h1b1", "h1a1"]
    },
    "test_resource_3": {
        "fen": "5k2/1R3p2/6p1/4N3/6Pp/2n2K1P/P2pr3/N6r b - - 1 42",
        "value": "r",
        "position": (4, 1),
        "expected_result": ["e2e3", "e2e4", "e2e5", "e2e1", "e2f2", "e2g2", "e2h2"]
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
    piece = Piece(test_data["value"], test_data["position"])
    actual_result = test_object.generate_rook_moves(piece)
    assert actual_result == test_data["expected_result"], (f"Failed on {test_key}, expected: "
                                                           f"{test_data['expected_result']}, actual: "
                                                           f"{actual_result}")
