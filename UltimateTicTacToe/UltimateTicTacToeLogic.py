'''
Board class for the game of TicTacToe.
Default board size is 3x3.
Board data:
  1=white(O), -1=black(X), 0=empty
  first dim is column , 2nd is row:
     pieces[0][0] is the top left square,
     pieces[2][0] is the bottom left square,
Squares are stored and manipulated as (x,y) tuples.

Author: Evgeny Tyurin, github.com/evg-tyurin
Date: Jan 5, 2018.

Based on the board for the game of Othello by Eric P. Nichols.

'''
import numpy as np

winning_combinations = [[0, 1, 2],
                        [3, 4, 5],
                        [6, 7, 8],
                        [0, 3, 6],
                        [1, 4, 7],
                        [2, 5, 8],
                        [0, 4, 8],
                        [2, 4, 6]]

class Board():

    def __init__(self, n=9):
        "Set up initial board configuration."

        self.n = n
        self.prev_move = n
        # Create the empty board array.
        self.pieces = [None]*self.n
        for i in range(self.n):
            self.pieces[i] = [0]*self.n

    # add [][] indexer syntax to the Board
    def __getitem__(self, index): 
        return self.pieces[index]

    def get_legal_moves(self, color):
        """Returns all the legal moves for the given color.
        (1 for white, -1 for black)
        @param color not used and came from previous version.        
        """
        moves = set()  # stores the legal moves.

        # Get all the empty squares (color==0)
        if self.prev_move < self.n and not (self.is_miniboard_win(self[self.prev_move], 1) or self.is_miniboard_win(self[self.prev_move], -1)):
            for x in range(self.n):
                if self[self.prev_move][x] == 0:
                    newmove = (self.prev_move, x)
                    moves.add(newmove)
            return list(moves)

        for y in range(self.n):
            if self.is_miniboard_win(self[y], 1) or self.is_miniboard_win(self[y], -1):
                continue
            for x in range(self.n):
                if self[x][y]==0:
                    newmove = (x,y)
                    moves.add(newmove)
        return list(moves)

    def has_legal_moves(self):
        for y in range(self.n):
            if self.is_miniboard_win(self[y], 1) or self.is_miniboard_win(self[y], -1):
                continue
            for x in range(self.n):
                if self[x][y] == 0:
                    return True
        return False
    
    def is_miniboard_win(self, miniboard_id, color):
        miniboard = self[miniboard_id]
        for combination in winning_combinations:
            if np.all(miniboard[combination] == color):
                return True
               
        return False

    def is_win(self, color):
        """Check whether the given player has collected a triplet in any direction; 
        @param color (1=white,-1=black)
        """
        
        for combination in winning_combinations:
            if self.is_miniboard_win(combination[0], color) and \
               self.is_miniboard_win(combination[1], color) and \
               self.is_miniboard_win(combination[2], color):
                return True
        
        return False

    def execute_move(self, move, color):
        """Perform the given move on the board; 
        color gives the color of the piece to play (1=white,-1=black)
        """

        (x,y) = move

        # Add the piece to the empty square.
        # assert self[x][y] == 0
        self[x][y] = color
        self.prev_move = y

