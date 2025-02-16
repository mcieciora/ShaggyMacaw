class Move:
    """Support class for move setup."""

    def __init__(
        self,
        original_square=None,
        is_move_legal=False,
        is_capture=False,
        is_en_passant=False,
        is_castling=False,
        is_promotion=False,
        promotion_piece=None,
        target_square=None,
        piece_value=None,
    ):
        self.original_square = original_square
        self.is_move_legal = is_move_legal
        self.is_capture = is_capture
        self.is_en_passant = is_en_passant
        self.is_castling = is_castling
        self.is_promotion = is_promotion
        self.promotion_piece = promotion_piece
        self.target_square = target_square
        self.piece_value = piece_value

    def __str__(self):
        """Return object in coordinates notation."""
        if self.is_promotion and self.is_capture:
            return f"{self.original_square}{self.target_square}={self.promotion_piece}"
        elif self.is_promotion:
            return f"{self.target_square}={self.promotion_piece}"
        else:
            return f"{self.original_square}{self.target_square}"
