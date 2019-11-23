"""
Pieces.py

Created by: Robert Sehlstedt
Last Edited: 2019-11-18

Implements pieces to the chess game.
"""

import numpy as np
from enum import Enum

DIR_UP = np.array((0, 1))
DIR_UP_RIGHT = np.array((1, 1))
DIR_RIGHT = np.array((1, 0))
DIR_DOWN_RIGHT = np.array((1, -1))
DIR_DOWN = np.array((0, -1))
DIR_DOWN_LEFT = np.array((-1, -1))
DIR_LEFT = np.array((-1, 0))
DIR_UP_LEFT = np.array((-1, 1))

class Color(Enum):
    WHITE = 0
    BLACK = 1
    NONE = 2

class Piece(object):
    """

    """
    symbol = 'X'
    dirs = ()
    
    def __init__(self, color):
        if color == Color.WHITE:
            self.string = self.symbol.upper()
        elif color == Color.BLACK:
            self.string = self.symbol.lower()
        elif color == Color.NONE:
            self.string = self.symbol
        else:
            self.string = "E" # ERROR

    def __repr__(self):
        return self.string

class Open(Piece):
    """

    """
    symbol = '-'
    dirs = ()
    def __init__(self):
        Piece.__init__(self, Color.NONE)

class Pawn(Piece):
    """

    """
    symbol = 'P'
    dirs = ()

class Rook(Piece):
    """

    """
    symbol = 'R'
    dirs = (DIR_UP, DIR_RIGHT, DIR_DOWN, DIR_LEFT)

class Knight(Piece):
    """

    """
    symbol = 'N'
    dirs = (DIR_UP + DIR_UP_RIGHT,
            DIR_RIGHT + DIR_UP_RIGHT,
            DIR_RIGHT + DIR_DOWN_RIGHT,
            DIR_DOWN + DIR_DOWN_RIGHT,
            DIR_DOWN + DIR_DOWN_LEFT,
            DIR_LEFT + DIR_DOWN_LEFT,
            DIR_LEFT + DIR_UP_LEFT,
            DIR_UP + DIR_UP_LEFT)

class Bishop(Piece):
    """

    """
    symbol = 'B'
    dirs = (DIR_UP_RIGHT, DIR_DOWN_RIGHT,
            DIR_DOWN_LEFT, DIR_UP_LEFT)

class Queen(Piece):
    """
    
    """
    symbol = 'Q'
    dirs = (DIR_UP, DIR_UP_RIGHT, DIR_RIGHT,
            DIR_DOWN_RIGHT, DIR_DOWN, DIR_DOWN_LEFT,
            DIR_LEFT, DIR_UP_LEFT)

class King(Piece):
    """

    """
    symbol = 'K'
    dirs = ()
