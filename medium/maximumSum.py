"""
https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/
You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j,
such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that
you can obtain over all possible indices i and j that satisfy the conditions.
Return -1 if there are no two numbers that satisfy the conditions.
"""
from typing import List


class Solution:
    @staticmethod
    def maximumSum(nums: List[int]) -> int:
        pass


if __name__ == '__main__':
    print(Solution.maximumSum(nums=[18, 43, 36, 13, 7]))  # 54
    # Explanation: The pairs (i, j) that satisfy the conditions are:
    # - (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
    # - (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
    # So the maximum sum that we can obtain is 54.
