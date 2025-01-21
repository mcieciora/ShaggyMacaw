expected_data = {
    "test_resource_1": {
        "board_setup": [
            ["r", "n", "", "q", "", "r", "k", ""],
            ["p", "b", "", "p", "p", "p", "b", "p"],
            ["", "p", "", "", "", "n", "p", ""],
            ["", "", "P", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "P", "", "", "P", "N", "", ""],
            ["P", "B", "P", "", "B", "P", "P", "P"],
            ["R", "N", "", "Q", "", "R", "K", ""]
        ],
        "white_move": False,
        "castling_rights": "-",
        "available_en_passant": "-",
        "half_move_clock": 0,
        "full_move_number": 8
    },
    "test_resource_2": {
        "board_setup": [
            ['r', '', '', 'q', '', 'r', 'k', ''],
            ['p', 'b', '', '', '', 'p', 'b', 'p'],
            ['', '', '', 'p', 'p', 'n', 'p', ''],
            ['', '', 'p', '', 'n', '', '', ''],
            ['', '', 'P', '', '', '', '', ''],
            ['', 'P', 'N', '', 'P', '', '', ''],
            ['P', 'B', 'Q', 'N', 'B', 'P', 'P', 'P'],
            ['R', '', '', '', '', 'R', 'K', '']
        ],
        "white_move": False,
        "castling_rights": "-",
        "available_en_passant": "-",
        "half_move_clock": 1,
        "full_move_number": 13
    },
    "test_resource_3": {
        "board_setup": [
            ['', '', 'r', 'r', '', '', 'k', ''],
            ['p', 'b', '', '', 'q', 'p', 'b', 'p'],
            ['', '', '', '', '', 'n', 'p', ''],
            ['', '', 'p', 'p', 'n', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', 'P', 'N', '', 'P', '', '', 'P'],
            ['P', 'B', 'Q', 'N', 'B', 'P', 'P', ''],
            ['', '', '', 'R', 'R', '', 'K', '']
        ],
        "white_move": True,
        "castling_rights": "-",
        "available_en_passant": "-",
        "half_move_clock": 0,
        "full_move_number": 18
    },
    "test_resource_4": {
        "board_setup": [
            ['r', '', '', '', 'r', '', 'k', ''],
            ['p', 'p', '', '', '', 'p', '', 'p'],
            ['', 'b', 'n', '', '', '', '', ''],
            ['', '', '', '', '', '', 'p', ''],
            ['', '', '', 'p', '', 'N', 'b', ''],
            ['', '', '', '', '', '', 'P', ''],
            ['P', 'P', '', 'N', 'P', 'P', 'B', 'P'],
            ['R', '', 'R', '', '', 'K', '', '']
        ],
        "white_move": True,
        "castling_rights": "-",
        "available_en_passant": "g6",
        "half_move_clock": 0,
        "full_move_number": 18
    },
    "test_resource_5": {
        "board_setup": [
            ['', '', 'r', '', '', '', 'k', ''],
            ['p', '', 'r', '', '', 'p', '', 'p'],
            ['', '', '', '', '', '', 'p', ''],
            ['', '', 'N', '', 'R', '', '', ''],
            ['', '', 'N', '', '', '', '', ''],
            ['', 'P', '', '', '', '', '', 'P'],
            ['P', '', '', '', '', 'P', '', ''],
            ['', '', '', '', '', '', 'K', '']
        ],
        "white_move": True,
        "castling_rights": "-",
        "available_en_passant": "-",
        "half_move_clock": 0,
        "full_move_number": 31
    },
    "test_resource_6": {
        "board_setup": [
            ['r', '', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', '', 'p', 'p', 'p', 'p', 'p'],
            ['', '', 'n', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', 'p', 'P', '', '', ''],
            ['', '', '', '', '', 'N', '', ''],
            ['P', 'P', 'P', '', '', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', '', 'R']
        ],
        "white_move": True,
        "castling_rights": "KQkq",
        "available_en_passant": "-",
        "half_move_clock": 0,
        "full_move_number": 4
    },
    "test_resource_7": {
        "board_setup": [
            ['r', '', 'b', 'q', 'k', '', 'n', 'r'],
            ['', 'p', '', '', '', 'p', 'b', 'p'],
            ['p', '', 'n', 'p', '', '', 'p', ''],
            ['', '', '', '', 'p', '', '', ''],
            ['', '', 'P', '', 'P', '', '', ''],
            ['', '', 'N', 'B', '', '', '', ''],
            ['P', 'P', '', '', '', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', '', '', 'R']
        ],
        "white_move": True,
        "castling_rights": "KQkq",
        "available_en_passant": "-",
        "half_move_clock": 2,
        "full_move_number": 9
    },
    "test_resource_8": {
        "board_setup": [
            ['', 'r', 'n', '', '', 'r', 'k', ''],
            ['', 'p', '', 'q', '', 'p', 'b', 'p'],
            ['p', '', 'n', 'p', 'b', '', 'p', ''],
            ['', '', '', 'N', 'p', '', '', ''],
            ['', '', 'P', '', 'P', '', '', ''],
            ['', '', 'N', 'B', 'B', '', '', ''],
            ['P', 'P', '', '', '', 'P', 'P', 'P'],
            ['R', '', '', 'Q', '', 'R', 'K', '']
        ],
        "white_move": True,
        "castling_rights": "-",
        "available_en_passant": "-",
        "half_move_clock": 14,
        "full_move_number": 15
    },
    "test_resource_9": {
        "board_setup": [
            ['', 'r', 'n', '', '', 'r', 'k', ''],
            ['', 'p', '', 'q', '', '', 'b', 'p'],
            ['p', '', '', 'p', 'b', '', 'p', ''],
            ['', '', '', 'N', '', '', '', ''],
            ['P', '', 'P', 'p', '', 'N', '', ''],
            ['', '', '', 'B', '', '', '', ''],
            ['', 'P', '', '', '', 'P', 'P', 'P'],
            ['R', '', '', 'Q', '', 'R', 'K', '']
        ],
        "white_move": False,
        "castling_rights": "-",
        "available_en_passant": "-",
        "half_move_clock": 3,
        "full_move_number": 21
    },
    "test_resource_10": {
        "board_setup": [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', 'P', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['P', 'P', 'P', 'P', '', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ],
        "white_move": False,
        "castling_rights": "KQkq",
        "available_en_passant": "e3",
        "half_move_clock": 0,
        "full_move_number": 1
    },
}