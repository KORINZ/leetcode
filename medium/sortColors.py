"""
https://leetcode.com/problems/sort-colors/
Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""
from typing import List


class Solution:
    @staticmethod
    def sortColors(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Quick Sort (one pass)
        left, right = 0, len(nums) - 1
        i = 0

        def swap(a: int, b: int) -> None:
            nums[a], nums[b] = nums[b], nums[a]

        while i <= right:
            if nums[i] == 0:
                swap(left, i)
                left += 1
            elif nums[i] == 2:
                swap(i, right)
                right -= 1
                i -= 1
            i += 1

        # Time complexity : O(N)
        # Space complexity : O(1)
