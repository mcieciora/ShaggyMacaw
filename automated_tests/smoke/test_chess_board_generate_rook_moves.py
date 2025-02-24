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
    },
    "test_resource_4": {
        "fen": "4qk2/2r3bp/1p1pb1p1/p4r2/1nPPpn2/2NB3P/5NP1/R1BQK2R w KQ - 2 9",
        "value": "R",
        "position": (0, 0),
        "expected_result": ["a1a2", "a1a3", "a1a4", "a1a5", "a1b1"]
    },
    "test_resource_5": {
        "fen": "4qk2/2r3bp/1p1pb1p1/p4r2/1nPPpn2/2NB3P/5NP1/R1BQK2R w KQ - 2 9",
        "value": "R",
        "position": (7, 0),
        "expected_result": ["h1h2", "h1g1", "h1f1"]
    },
    "test_resource_6": {
        "fen": "4qk2/2r3bp/1p1pb1p1/p4r2/1nPPpn2/2NB3P/5NP1/R1BQK2R w KQ - 2 9",
        "value": "r",
        "position": (2, 6),
        "expected_result": ["c7c8", "c7c6", "c7c5", "c7c4", "c7d7", "c7e7", "c7f7", "c7b7", "c7a7"]
    },
    "test_resource_7": {
        "fen": "4qk2/2r3bp/1p1pb1p1/p4r2/1nPPpn2/2NB3P/5NP1/R1BQK2R w KQ - 2 9",
        "value": "r",
        "position": (5, 4),
        "expected_result": ["f5f6", "f5f7", "f5g5", "f5h5", "f5e5", "f5d5", "f5c5", "f5b5"]
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
    actual_result = test_object.generate_piece_moves(piece)
    assert [str(result) for result in actual_result] == expected_output, \
        f"Failed on {test_key}, expected: {expected_output}, actual: {actual_result}"
