from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def isValidSudoku(board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True


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
    print(Solution.isValidSudoku(board))
