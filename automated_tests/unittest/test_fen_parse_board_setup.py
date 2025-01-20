from pytest import mark, raises

from src.fen import Fen, WrongBoardSize


@mark.unittest
def test__fen__parse_board_setup():
    """Cover tc-0"""
    expected_data = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    test_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    test_object = Fen(original_fen)
    test_data = test_object.parse_board_setup(test_fen)
    for row_index, row in enumerate(test_data):
        for square_index, square in enumerate(row):
            expected_square = expected_data[row_index][square_index]
            assert square == expected_square, f"Expected: {expected_square}, actual: {square}"


@mark.unittest
def test__fen__parse_board_setup__insufficient_rows():
    """Cover tc-0"""
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    test_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP"
    test_object = Fen(original_fen)

    with raises(WrongBoardSize):
        test_object.parse_board_setup(test_fen)


@mark.unittest
def test__fen__parse_board_setup__insufficient_files():
    """Cover tc-0"""
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    test_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBN"
    test_object = Fen(original_fen)

    with raises(WrongBoardSize):
        test_object.parse_board_setup(test_fen)