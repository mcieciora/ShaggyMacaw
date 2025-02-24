from pytest import mark

from src.fen import Fen
from src.move import Move


@mark.unittest
def test__unittest__fen__update_castling_rights__queen_side_rook_moves():
    original_fen = "r3kb1r/pp1q1ppp/2n1bn2/2pp4/1P1P4/B1N2NP1/P2QPPBP/R3K2R w KQkq - 2 7"
    test_data_dict = {
        "r": {
            "squares": [("a8", "b8"), ("a8", "c8"), ("a8", "d8")],
            "expected_value": "KQk"
        },
        "R": {
            "squares": [("a1", "b1"), ("a1", "c1"), ("a1", "d1")],
            "expected_value": "Kkq"
        }
    }
    for piece_value, test_data in test_data_dict.items():
        for squares in test_data["squares"]:
            test_object = Fen(original_fen)
            move = Move(original_square=squares[0], target_square=squares[1], piece_value=piece_value)
            test_object.update_castling_rights(move)
            actual_data = test_object.castling_rights
            assert actual_data == test_data["expected_value"], (f"Expected: {test_data['expected_value']}, "
                                                                f"actual: {actual_data}")


@mark.unittest
def test__unittest__fen__update_castling_rights__king_side_rook_moves():
    original_fen = "r3kb1r/pp1q1ppp/2n1bn2/2pp4/1P1P4/B1N2NP1/P2QPPBP/R3K2R w KQkq - 2 7"
    test_data_dict = {
        "r": {
            "squares": [("h8", "g8")],
            "expected_value": "KQq"
        },
        "R": {
            "squares": [("h1", "g1"), ("h1", "f1")],
            "expected_value": "Qkq"
        }
    }
    for piece_value, test_data in test_data_dict.items():
        for squares in test_data["squares"]:
            test_object = Fen(original_fen)
            move = Move(original_square=squares[0], target_square=squares[1], piece_value=piece_value)
            test_object.update_castling_rights(move)
            actual_data = test_object.castling_rights
            assert actual_data == test_data["expected_value"], (f"Expected: {test_data['expected_value']}, "
                                                                f"actual: {actual_data}")


@mark.unittest
def test__unittest__fen__update_castling_rights__king_moves():
    original_fen = "r3kb1r/pp1q1ppp/2n1bn2/2pp4/1P1P4/B1N2NP1/P2QPPBP/R3K2R w KQkq - 2 7"
    test_data_dict = {
        "k": {
            "squares": [("e8", "d8"), ("e8", "e7")],
            "expected_value": "KQ"
        },
        "K": {
            "squares": [("e1", "d1"), ("e1", "f1")],
            "expected_value": "kq"
        }
    }
    for piece_value, test_data in test_data_dict.items():
        for squares in test_data["squares"]:
            test_object = Fen(original_fen)
            move = Move(original_square=squares[0], target_square=squares[1], piece_value=piece_value)
            test_object.update_castling_rights(move)
            actual_data = test_object.castling_rights
            assert actual_data == test_data["expected_value"], (f"Expected: {test_data['expected_value']}, "
                                                                f"actual: {actual_data}")


@mark.unittest
def test__unittest__fen__update_castling_rights__empty_castling_rights():
    original_fen = "2kr1b1r/pp1q1ppp/2n1bn2/2pp4/1P1P4/B1N2NP1/P2QPP1P/R3KBR1 w Q - 2 7"
    test_object = Fen(original_fen)
    move = Move(original_square="a1", target_square="b1", piece_value="R")
    test_object.update_castling_rights(move)
    actual_data = test_object.castling_rights
    assert actual_data == "-", f"Expected: -, actual: {actual_data}"
