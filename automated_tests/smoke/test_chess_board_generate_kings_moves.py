from pytest import mark

from src.chess_board import ChessBoard

test_data_dict = {
    # FIXME Fails on active_colour == False trying to take b3 while its defended by b2
    "test_resource_1": {
        "fen": "8/8/p7/1p6/1k6/1P6/1K6/8 w - - 0 58",
        "value": "k",
        "square": "b4",
        "expected_result": ["b4a5", "b4c5"]
    },
    "test_resource_2": {
        "fen": "8/8/p7/1p6/1k6/1P6/1K6/8 w - - 0 58",
        "value": "K",
        "square": "b2",
        "expected_result": ["b2a2", "b2a1", "b2b1", "b2c1", "b2c2"]
    },
    # FIXME Fails on active_colour == False trying to take g4 while its defended by h3
    "test_resource_3": {
        "fen": "4R3/5p1N/6p1/8/3p1kPp/2n4P/P2r4/4K3 b - - 21 52",
        "value": "k",
        "square": "f4",
        "expected_result": ["f4f3", "f4g3"]
    },
    "test_resource_4": {
        "fen": "4R3/5p1N/6p1/8/3p1kPp/2n4P/P2r4/4K3 b - - 21 52",
        "value": "K",
        "square": "e1",
        "expected_result": ["e1d2", "e1f1"]
    },
    "test_resource_5": {
        "fen": "r3k1nr/1pbq1pbp/p1np2p1/4p3/2P1P3/2NB4/PP3PPP/RNBQK2R w KQkq - 2 9",
        "value": "k",
        "square": "e8",
        "expected_result": ["e8f8", "e8d8", "e8c8", "e8e7"]
    },
    "test_resource_6": {
        "fen": "r1bqk1nr/1p3pbp/p1np2p1/4p3/2P1P3/2NB4/PP3PPP/RNBQK2R w KQkq - 2 9",
        "value": "K",
        "square": "e1",
        "expected_result": ["e1d2", "e1e2", "e1f1", "e1g1"]
    },
    "test_resource_7": {
        "fen": "3rkb1r/pB5p/5p2/2p2b2/8/6P1/RP2PP1P/2B1K2R b Kk - 2 7",
        "value": "k",
        "square": "e8",
        "expected_result": ["e8d7", "e8e7", "e8f7"]
    },
    "test_resource_8": {
        "fen": "3rkb1r/pB5p/5p2/2p2b2/8/6P1/RP2PP1P/2B1K2R b Kk - 2 7",
        "value": "K",
        "square": "e1",
        "expected_result": ["e1f1", "e1g1"]
    },
    "test_resource_9": {
        "fen": "r3k1r1/pB5p/5p2/2B2b2/8/8/RP2P3/4K2R b Kq - 2 7",
        "value": "k",
        "square": "e8",
        "expected_result": ["e8d8", "e8d7", "e8f7"]
    },
    "test_resource_10": {
        "fen": "r3k1r1/pB5p/5p2/2p2b2/8/8/RP2P3/2B1K2R w Kq - 2 7",
        "value": "K",
        "square": "e1",
        "expected_result": ["e1f1", "e1d1", "e1f2", "e1d2"]
    },
}


def get_parametrized_test_set():
    parametrized_test_set_list = []
    for test_key, test_data in test_data_dict.items():
        parametrized_test_set_list.append((test_key, test_data, test_data["expected_result"]))
    return parametrized_test_set_list


@mark.smoke
@mark.parametrize("test_key,test_data,expected_output", get_parametrized_test_set(), ids=test_data_dict.keys())
def test__smoke__chess_board__generate_kings_moves(test_key, test_data, expected_output):
    test_object = ChessBoard(test_data["fen"])
    actual_data = test_object.generate_all_possible_moves()
    king_moves = [move for move in actual_data if move.startswith(test_data["square"])]
    king_moves_number = len(king_moves)

    expected_data = len(test_data["expected_result"])
    assert king_moves_number == expected_data, f"Expected: {test_data['expected_result']}, actual: {king_moves}"

    for move in test_data['expected_result']:
        assert move in actual_data, f"Expected: {move} not in {actual_data}"
