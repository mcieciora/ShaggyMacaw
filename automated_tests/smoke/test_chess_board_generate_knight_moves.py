from pytest import mark

from src.chess_board import ChessBoard
from src.piece import Piece

test_data_dict = {
    "test_resource_1": {
        "fen": "5k2/1R3p2/6p1/4N3/6Pp/2n2K1P/P2pr3/N7 b - - 1 42",
        "value": "n",
        "position": (2, 2),
        "expected_result": ["c3e4", "c3d5", "c3d1", "c3a4", "c3b5", "c3a2", "c3b1"]
    },
    "test_resource_2": {
        "fen": "5k2/1R3p2/6p1/4N3/6Pp/2n2K1P/P2pr3/N6r b - - 1 42",
        "value": "N",
        "position": (0, 0),
        "expected_result": ["a1c2", "a1b3"]
    },
    "test_resource_3": {
        "fen": "5k2/1R3p2/6p1/4N3/6Pp/2n2K1P/P2pr3/N6r b - - 1 42",
        "value": "N",
        "position": (4, 4),
        "expected_result": ["e5g6", "e5f7", "e5c6", "e5d7", "e5c4", "e5d3"]
    },
    "test_resource_4": {
        "fen": "4qk2/2r3bp/1p1pb1p1/p4r2/1nPPpn2/2NB3P/5NP1/R1BQK2R w KQ - 2 9",
        "value": "n",
        "position": (1, 3),
        "expected_result": ["b4d5", "b4c6", "b4d3", "b4c2", "b4a6", "b4a2"]
    },
    "test_resource_5": {
        "fen": "4qk2/2r3bp/1p1pb1p1/p4r2/1nPPpn2/2NB3P/5NP1/R1BQK2R w KQ - 2 9",
        "value": "n",
        "position": (5, 3),
        "expected_result": ["f4h5", "f4h3", "f4g2", "f4d5", "f4d3", "f4e2"]
    },
    "test_resource_6": {
        "fen": "4qk2/2r3bp/1p1pb1p1/p4r2/1nPPpn2/2NB3P/5NP1/R1BQK2R w KQ - 2 9",
        "value": "N",
        "position": (2, 2),
        "expected_result": ["c3e4", "c3d5", "c3e2", "c3a4", "c3b5", "c3a2", "c3b1"]
    },
    "test_resource_7": {
        "fen": "4qk2/2r3bp/1p1pb1p1/p4r2/1nPPpn2/2NB3P/5NP1/R1BQK2R w KQ - 2 9",
        "value": "N",
        "position": (5, 1),
        "expected_result": ["f2g4", "f2e4"]
    }
}


def get_parametrized_test_set():
    parametrized_test_set_list = []
    for test_key, test_data in test_data_dict.items():
        parametrized_test_set_list.append((test_key, test_data, test_data["expected_result"]))
    return parametrized_test_set_list


@mark.smoke
@mark.parametrize("test_key,test_data,expected_output", get_parametrized_test_set(), ids=test_data_dict.keys())
def test__smoke__chess_board__generate_piece_moves(test_key, test_data, expected_output):
    test_object = ChessBoard(test_data["fen"])
    piece = Piece(test_data["value"], test_data["position"])
    actual_result = test_object.generate_piece_moves(piece, not_continuous_movement=True)
    assert [str(result) for result in actual_result] == expected_output, \
        f"Failed on {test_key}, expected: {expected_output}, actual: {actual_result}"
