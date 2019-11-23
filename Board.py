"""
Board.py

Created by: Robert Sehlstedt
Last Edited: 2019-11-18

Implements the board to the game.
"""

import numpy as np

from Pieces import *

BOARD_DIMENSION = (8, 8) # Width, Height
W = Color.WHITE
B = Color.BLACK

LETTERS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')


class Board(object):
    """
    
    """
    def __init__(self):
        self.board = _create_board_()

    def __str__(self):
        s = ""
        
        for n in range(BOARD_DIMENSION[1] -1, -1, -1):
            
            s += str(n+1)
            s += "|"
            
            for m in range(BOARD_DIMENSION[0]):
                s += str(self.board[n, m])
                s += " "
                
            s += "\n"

        s += "  "
        s += "-" * 2 * BOARD_DIMENSION[0]
        s += "\n"
        s += "  "
            
        for c in LETTERS:
            s += c
            s += " "
            
        return s
           

def _create_board_():
    return np.array(
        [[Rook(W), Bishop(W), Knight(W), Queen(W),
          King(W), Knight(W), Bishop(W), Rook(W)],

         [Pawn(W), Pawn(W), Pawn(W), Pawn(W),
          Pawn(W), Pawn(W), Pawn(W), Pawn(W)],

         [Open(), Open(), Open(), Open(),
          Open(), Open(), Open(), Open()],

         [Open(), Open(), Open(), Open(),
          Open(), Open(), Open(), Open()],

         [Open(), Open(), Open(), Open(),
          Open(), Open(), Open(), Open()],

         [Open(), Open(), Open(), Open(),
          Open(), Open(), Open(), Open()],

         [Pawn(B), Pawn(B), Pawn(B), Pawn(B),
          Pawn(B), Pawn(B), Pawn(B), Pawn(B)],

         [Rook(B), Bishop(B), Knight(B), Queen(B),
          King(B), Knight(B), Bishop(B), Rook(B)]])
