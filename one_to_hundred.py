"""
title: "One to hundred"
author: qkzk
date: 2022/02/04
"""
from copy import deepcopy


class Board:
    """
    Holds the dimension, the grid and the status of the game (finished or not).
    If a solution is found, it's saved.
    """

    def __init__(self, width: int = 10, height: int = 10):
        self.width = width
        self.height = height
        self.grid = [[0] * self.width for _ in range(self.height)]
        self.finished = False
        self.max_reached = 0
        self.solution: list[list[int]]

    def possible_neighbors(self, i: int, j: int) -> tuple:
        """
        Two cells are "neighbors" if
            * they are separated by 2 empty cells on a straight line :
                10 . . 11
            * or one cell diagonally :
                10 .  .
                .  .  .
                .  .  11

        The order matter ! Other orders generates solution much slowlly.
        """
        return (
            (i, j + 3),
            (i + 3, j),
            (i, j - 3),
            (i - 3, j),
            (i - 2, j + 2),
            (i + 2, j + 2),
            (i + 2, j - 2),
            (i - 2, j - 2),
        )

    def valid_moves(self, i: int, j: int) -> filter:
        """
        Returns a filtered generator of neighbors.
        """
        return filter(self.valid_move, self.possible_neighbors(i, j))

    def valid_move(self, neib: tuple[int, int]) -> bool:
        """True iff a move is valid."""
        return self.inside(*neib) and self.empty_cell(*neib)

    def inside(self, i: int, j: int) -> bool:
        """True if those coords are inside the grid."""
        return 0 <= i < self.width and 0 <= j < self.height

    def empty_cell(self, i: int, j: int) -> bool:
        """True if there's a 0 in that cell"""
        return self.grid[j][i] == 0

    def play(self, i: int, j: int, current: int):
        """Mark a cell with current number"""
        self.grid[j][i] = current

    def unplay(self, i, j):
        """Put a 0 in this cell."""
        self.grid[j][i] = 0

    def update_max_reached(self, current: int):
        """Save the new best value reached, print the board."""
        if current > self.max_reached:
            self.max_reached = current
            print(current)
            print(self)

    def __repr__(self):
        return self.format_board(self.grid)

    def format_board(self, grid: list[list[int]]) -> str:
        """Format a board. It's used to display the best solution found"""
        s = []
        for line in grid:
            s.append("\n" + "".join(f"{val: 3d}" for val in line))
        return "".join(s)


def explore(board: Board, i: int, j: int, current: int = 2):
    """Explore the board, looking for a solution."""
    if board.finished or current > 100:
        if not board.finished:
            board.finished = True
            board.solution = deepcopy(board.grid)
        return

    for x, y in board.valid_moves(i, j):
        if board.finished:
            return

        board.play(x, y, current)
        board.update_max_reached(current)

        explore(board, x, y, current + 1)

        board.unplay(x, y)


def main():
    """Creates a board, start from top left and explore untill it finds a solution."""
    board = Board()
    board.play(0, 0, 1)
    explore(board, 0, 0)
    print(board.finished)
    print(board.format_board(board.solution))


if __name__ == "__main__":
    main()
