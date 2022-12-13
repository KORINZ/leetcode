"""
https://leetcode.com/problems/equal-row-and-column-pairs/
Given a 0-indexed n x n integer matrix grid,
return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
"""
from typing import List


class Solution:
    @staticmethod
    def equalPairs(grid: List[List[int]]) -> int:
        pass


if __name__ == '__main__':
    print(Solution.equalPairs(grid=[[3, 2, 1], [1, 7, 6], [2, 7, 7]]))  # 1
    # Explanation: There is 1 equal row and column pair:
    # - (Row 2, Column 1): [2,7,7]
