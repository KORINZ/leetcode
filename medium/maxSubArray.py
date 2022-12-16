"""
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the subarray which has the largest sum and return its sum.
"""
from typing import List


class Solution:
    @staticmethod
    def maxSubArray(nums: List[int]) -> int:
        max_sum, curr_sum = nums[0], 0

        for n in nums:
            curr_sum = max(curr_sum, 0) + n
            max_sum = max(max_sum, curr_sum)

        return max_sum


# Kadane's Algorithm
# Time Complexity: O(n)
# Memory Complexity: O(1)

if __name__ == '__main__':
    print(Solution.maxSubArray(nums=[5, 4, -1, 7, 8]))  # 23
