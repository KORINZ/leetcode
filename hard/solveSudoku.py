from collections import defaultdict
from typing import List, Tuple

STRING_NUMBERS = [str(n) for n in range(1, 10)]


class Solution:
    @staticmethod
    def solveSudoku(board: List[List[str]]) -> None:

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        # Place existing numbers to the gird
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col])
                    boxes[(row // 3, col // 3)].add(board[row][col])

        # Check if a number can be placed according to the constraints
        def can_place_number(r: int, c: int, num: str) -> bool:
            if (num in rows[r]) or (num in cols[c]) or (num in boxes[(r // 3, c // 3)]):
                return False
            else:
                return True

        def place_number_in_cell(r: int, c: int, num: str) -> None:
            board[r][c] = num
            rows[r].add(num)
            cols[c].add(num)
            boxes[(r // 3, c // 3)].add(num)

        def remove_number_in_cell(r: int, c: int, num: str) -> None:
            board[r][c] = "."
            rows[r].remove(num)
            cols[c].remove(num)
            boxes[(r // 3, c // 3)].remove(num)

        def move_to_next_cell(r: int, c: int) -> Tuple[int, int]:
            # Move to next column
            if c < 8:
                new_r, new_c = r, c + 1
            # Move to next row, reset column index
            else:
                new_r, new_c = r + 1, 0
            return new_r, new_c

        def backtrack(r: int, c: int) -> bool:
            # Base case: reached last row + 1
            if r > 8:
                return True

            # If a number already existed in the cell, move to the next cell
            if board[r][c] != ".":
                new_r, new_c = move_to_next_cell(r, c)
                return backtrack(new_r, new_c)

            # If a number can be placed, place it to the board
            for num in STRING_NUMBERS:
                if can_place_number(r, c, num):
                    place_number_in_cell(r, c, num)
                    if backtrack(r, c):
                        return True
                    else:
                        remove_number_in_cell(r, c, num)

            # The sudoku is not solvable
            return False

        backtrack(0, 0)


if __name__ == '__main__':
    input_board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                   ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                   [".", "9", "8", ".", ".", ".", ".", "6", "."],
                   ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                   ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                   ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                   [".", "6", ".", ".", ".", ".", "2", "8", "."],
                   [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                   [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    Solution.solveSudoku(input_board)
    for arr in input_board:
        print(arr)
