from pytest import mark

from src.chess_board import ChessBoard
from src.piece import Piece

test_data_dict = {
    "test_resource_1": {
        "fen": "8/8/p7/1p6/1k6/1P6/1K6/8 w - - 0 58",
        "value": "k",
        "position": (1, 3),
        "expected_result": ["b4a5", "b4c5"]
    },
    "test_resource_2": {
        "fen": "8/8/p7/1p6/1k6/1P6/1K6/8 w - - 0 58",
        "value": "K",
        "position": (1, 1),
        "expected_result": ["b2a2", "b2a1", "b2b1", "b2c1", "b2c2"]
    },
    "test_resource_3": {
        "fen": "4R3/5p1N/6p1/8/3p1kPp/2n4P/P2r4/4K3 b - - 21 52",
        "value": "k",
        "position": (5, 3),
        "expected_result": ["f4f3", "f4g3"]
    },
    "test_resource_4": {
        "fen": "4R3/5p1N/6p1/8/3p1kPp/2n4P/P2r4/4K3 b - - 21 52",
        "value": "K",
        "position": (4, 0),
        "expected_result": ["e1d2", "e1f1"]
    },
    "test_resource_5": {
        "fen": "r3k1nr/1pbq1pbp/p1np2p1/4p3/2P1P3/2NB4/PP3PPP/RNBQK2R w KQkq - 2 9",
        "value": "k",
        "position": (4, 7),
        "expected_result": ["e8f8", "e8d8", "e8c8", "e8e7"]
    },
    "test_resource_6": {
        "fen": "r1bqk1nr/1p3pbp/p1np2p1/4p3/2P1P3/2NB4/PP3PPP/RNBQK2R w KQkq - 2 9",
        "value": "K",
        "position": (4, 0),
        "expected_result": ["e1d2", "e1e2", "e1f1", "e1g1"]
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
    actual_result = test_object.generate_king_moves(piece)
    assert actual_result == test_data["expected_result"], (f"Failed on {test_key}, expected: "
                                                           f"{test_data['expected_result']}, actual: "
                                                           f"{actual_result}")
