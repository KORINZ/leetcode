"""
https://leetcode.com/problems/3sum/
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
from typing import List


class Solution:
    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        pass


if __name__ == '__main__':
    print(Solution.threeSum(nums=[-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
    # Explanation:
    # nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    # nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    # nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    # The distinct triplets are [-1,0,1] and [-1,-1,2].
    # Notice that the order of the output and the order of the triplets does not matter.
