from pytest import mark

from src.chess_board import ChessBoard
from src.piece import Piece


test_data_dict = {
    "test_resource_1": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "value": "Q",
        "position": (2, 1),
        "expected_result": ["c2d1", "c2b3", "c2a4", "c2b1", "c2c3", "c2c1", "c2d2", "c2b2"]
    },
    "test_resource_2": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "value": "q",
        "position": (3, 5),
        "expected_result": ["d6e7", "d6f8", "d6e5", "d6f4", "d6g3", "d6h2", "d6c5", "d6d7", "d6d8", "d6d5", "d6e6"]
    },
    "test_resource_3": {
        "fen": "4qk2/2r3bp/1p1pb1p1/p4r2/1nPPpn2/2NB3P/5NP1/R1BQK2R w KQ - 2 9",
        "value": "Q",
        "position": (3, 0),
        "expected_result": ["d1e2", "d1f3", "d1g4", "d1h5", "d1c2", "d1b3", "d1a4", "d1d2"]
    },
    "test_resource_4": {
        "fen": "4qk2/2r3bp/1p1pb1p1/p4r2/1nPPpn2/2NB3P/5NP1/R1BQK2R w KQ - 2 9",
        "value": "q",
        "position": (4, 7),
        "expected_result": ["e8f7", "e8d7", "e8c6", "e8b5", "e8a4", "e8e7", "e8d8", "e8c8", "e8b8", "e8a8"]
    }
}


def get_parametrized_test_set():
    parametrized_test_set_list = []
    for test_key, test_data in test_data_dict.items():
        parametrized_test_set_list.append((test_key, test_data, test_data["expected_result"]))
    return parametrized_test_set_list


@mark.smoke
@mark.parametrize("test_key,test_data,expected_output", get_parametrized_test_set(), ids=test_data_dict.keys())
def test__smoke__chess_board__generate_queen_moves(test_key, test_data, expected_output):
    test_object = ChessBoard(test_data["fen"])
    piece = Piece(test_data["value"], test_data["position"])
    actual_result = test_object.generate_piece_moves(piece)
    assert [str(result) for result in actual_result] == expected_output, \
        f"Failed on {test_key}, expected: {expected_output}, actual: {actual_result}"
