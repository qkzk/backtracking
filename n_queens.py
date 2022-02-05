"""
title: n queens
author: qkzk
date: 2021/02/05
"""

from copy import deepcopy
from itertools import product
from typing import Generator
from string import ascii_lowercase


class Board:
    """
    Holds the size, the board, the status (solved or not) of the game.
    If a solution is found, it's saved.
    """

    def __init__(self, size=8) -> None:
        self.size = size
        self.board = [[0] * self.size for _ in range(self.size)]
        self.solved = False
        self.max_reached = 0
        self.solution: list[list[int]]

    def play(self, row: int, col: int):
        """Put a queen in that square"""
        self.board[row][col] = 1

    def unplay(self, row: int, col: int):
        """Remove the queen from that square"""
        self.board[row][col] = 0

    def is_valid(self, row, col) -> bool:
        """True if there's at most one queen per row, col and diagonal"""
        return (
            self.is_valid_row(row)
            and self.is_valid_col(col)
            and self.is_valid_diag(row, col)
        )

    def is_valid_row(self, row: int) -> bool:
        """True if there's at most one queen on that row"""
        return sum(self.board[row]) <= 1

    def is_valid_col(self, col: int) -> bool:
        """True if there's at most one queen on that column"""
        return sum(self.board[row][col] for row in range(self.size)) <= 1

    def is_valid_diag(self, row: int, col: int) -> bool:
        """True if there's at most one queen on the diagonals crossing this square"""
        return self.is_valid_north_east(row, col) and self.is_valid_south_east(row, col)

    def north_east_diag(self, row: int, col: int) -> Generator:
        """Generate a NE direction diagonal"""
        diag = row + col
        return (
            (i, diag - i)
            for i in range(1 - 2 * self.size, 2 * self.size)
            if 0 <= i < self.size and 0 <= diag - i < self.size
        )

    def south_east_diag(self, row: int, col: int) -> Generator:
        """Generate a SE direction diagonal"""
        diag = row - col
        return (
            (diag + i, i)
            for i in range(1 - self.size, self.size)
            if 0 <= i < self.size and 0 <= diag + i < self.size
        )

    def is_valid_north_east(self, row: int, col: int):
        """True if there's at most one queen in the NE diagonal going through this square."""
        diag = self.north_east_diag(row, col)
        return sum(self.board[i][j] for i, j in diag) <= 1

    def is_valid_south_east(self, row: int, col: int):
        """True if there's at most one queen in the NE diagonal going through this square."""
        diag = self.south_east_diag(row, col)
        return sum(self.board[i][j] for i, j in diag) <= 1

    def update_max_reached(self, current: int):
        """Save the new best value reached, print the board."""
        if current > self.max_reached:
            self.max_reached = current
            print(current)
            print(self)

    def __repr__(self):
        return self.format_board(self.board)

    def format_board(self, board):
        """Format a board to be printed in the terminal"""
        string = "\n\n       " + " ".join(ascii_lowercase)[: 2 * self.size]
        for row, line in enumerate(board):
            string += f"\n    {self.size - row:>2}"
            for cell in line:
                if cell:
                    string += " ♛"
                else:
                    string += " ."
        return string + "\n"


def explore(board: Board, current: int = 0):
    """Explore the board, looking for a solution."""
    if board.solved or current >= board.size:
        if not board.solved:
            board.solved = True
            board.solution = deepcopy(board.board)
        return

    for row, col in product(range(board.size), repeat=2):
        if board.solved:
            return
        if board.board[row][col] == 1:
            continue
        board.play(row, col)
        if board.is_valid(row, col):
            explore(board, current + 1)
            board.update_max_reached(current)
        board.unplay(row, col)


def test():
    board = Board(8)
    row = 0
    col = 0
    print(row, col, list(board.north_east_diag(row, col)))
    print(row, col, list(board.south_east_diag(row, col)))
    board.play(2, 1)
    board.play(1, 2)
    print(board)
    print(board.is_valid_diag(1, 2))


def main():
    board = Board(10)
    explore(board)
    print(board.format_board(board.solution))


if __name__ == "__main__":
    # test()
    main()
