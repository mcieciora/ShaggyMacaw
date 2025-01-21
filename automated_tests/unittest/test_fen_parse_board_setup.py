from pytest import mark, raises

from src.fen import Fen, WrongBoardSize


@mark.unittest
def test__unittest__fen__parse_board_setup():
    expected_data = "rnbqkbnrpppppppp--------------------------------PPPPPPPPRNBQKBNR"
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    test_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    test_object = Fen(original_fen)
    actual_data = test_object.parse_board_setup(test_fen)
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__fen__parse_board_setup__insufficient_rows():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    test_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP"
    test_object = Fen(original_fen)

    with raises(WrongBoardSize):
        test_object.parse_board_setup(test_fen)


@mark.unittest
def test__unittest__fen__parse_board_setup__insufficient_files():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    test_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBN"
    test_object = Fen(original_fen)

    with raises(WrongBoardSize):
        test_object.parse_board_setup(test_fen)
