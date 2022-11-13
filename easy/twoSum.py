"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        stored_values = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in stored_values:
                return [stored_values[diff], i]
            stored_values[n] = i


if __name__ == '__main__':
    print(Solution().twoSum(nums=[2, 7, 11, 15], target=26))  # [2, 3] since 11+15=26

# Time Complexity: O(n)
# Memory Complexity: O(n)
