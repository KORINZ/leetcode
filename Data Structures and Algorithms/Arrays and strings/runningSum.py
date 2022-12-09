"""
https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4658/
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
"""
from typing import List


class Solution:
    @staticmethod
    def runningSum(nums: List[int]) -> List[int]:
        prefix = nums[0]

        for i, n in enumerate(nums[1:], start=1):
            nums[i] += prefix
            prefix += n

        return nums


if __name__ == '__main__':
    print(Solution.runningSum(nums=[1, 2, 3, 4]))  # [1, 3, 6, 10]
