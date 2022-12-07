"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""
from typing import List


class Solution:
    @staticmethod
    def reverseString(s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Two pointers
        left, right = 0, len(s) - 1
