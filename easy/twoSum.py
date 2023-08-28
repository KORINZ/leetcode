"""
https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

from typing import List, Union


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> Union[List[int], None]:
        stored_values = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in stored_values:
                return [stored_values[diff], i]
            stored_values[n] = i

    # Time Complexity: O(n)
    # Memory Complexity: O(n)

    @staticmethod
    def twoSum_brute(nums: List[int], target: int) -> Union[List[int], None]:

        for i, n in enumerate(nums):
            for j, m in enumerate(nums[i + 1:]):
                if target == n + m:
                    return [i, i + j + 1]

    # brute force solution
    # Time Complexity: O(n^2)
    # Memory Complexity: O(1)


if __name__ == '__main__':
    # [2, 3] since 11+15=26
    print(Solution().twoSum(nums=[2, 7, 11, 15], target=26))
    # [2, 3] since 11+15=26
    print(Solution().twoSum_brute(nums=[2, 7, 11, 15], target=26))
