"""
https://leetcode.com/problems/equal-row-and-column-pairs/
Given a 0-indexed n x n integer matrix grid,
return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
"""
from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def equalPairs(grid: List[List[int]]) -> int:

        # rows
        dic_row = defaultdict(int)
        for row in grid:
            dic_row[tuple(row)] += 1

        # columns
        dic_col = defaultdict(int)
        for col in range(len(grid[0])):
            curr_col = []
            for row in range(len(grid)):
                curr_col.append(grid[row][col])

            dic_col[tuple(curr_col)] += 1

        ans = 0
        for arr in dic_row:
            ans += dic_row[arr] * dic_col[arr]

        return ans

    # Time complexity : O(n^2)
    # Space complexity : O(n^2)


if __name__ == '__main__':
    print(Solution.equalPairs(grid=[[3, 2, 1], [1, 7, 6], [2, 7, 7]]))  # 1
    # Explanation: There is 1 equal row and column pair:
    # - (Row 2, Column 1): [2,7,7]
