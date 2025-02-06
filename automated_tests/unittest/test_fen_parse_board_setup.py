from pytest import mark, raises

from src.fen import Fen, WrongBoardSize
from src.piece import Pawn, Piece
from src.piece import PieceType


@mark.unittest
def test__unittest__fen__parse_board_setup():
    expected_data = {
        PieceType.EMPTY: 32,
        PieceType.PAWN: 16,
        PieceType.KNIGHT: 4,
        PieceType.BISHOP: 4,
        PieceType.ROOK: 4,
        PieceType.QUEEN: 2,
        PieceType.KING: 2
    }
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    test_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    test_object = Fen(original_fen)
    return_data = [square.piece_type if type(square) in [Pawn, Piece] else square
                   for square in sum(test_object.parse_board_setup(test_fen), [])]
    for square_value, test_data in expected_data.items():
        actual_data = return_data.count(square_value)
        assert actual_data == test_data, f"Expected: {test_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__fen__parse_board_setup__insufficient_ranks():
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
