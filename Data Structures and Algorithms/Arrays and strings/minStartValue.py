"""
https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4657/
Given an array of integers nums, you start with an initial positive value startValue.
In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
Return the minimum positive value of startValue such that the step by step sum is never less than 1.
"""
from typing import List


class Solution:
    @staticmethod
    def runningSum(nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        return nums

    @staticmethod
    def minStartValue(nums: List[int]) -> int:
        nums = Solution.runningSum(nums)
        smallest = min(nums)
        if smallest >= 1:
            return 1
        else:
            return abs(smallest) + 1

    # Prefix total approach
    # Time complexity: O(n)
    # Space complexity: O(1)


if __name__ == '__main__':
    print(Solution.minStartValue(nums=[-3, 2, -3, 4, 2]))  # 5
