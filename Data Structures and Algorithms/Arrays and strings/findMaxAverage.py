"""
https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4594/
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.
"""
from typing import List


class Solution:
    @staticmethod
    def findMaxAverage(nums: List[int], k: int) -> float:
        l, r = 0, k
        ans = curr = sum(nums[l:k])

        while r < len(nums):
            curr += nums[r] - nums[l]

            if curr > ans:
                ans = curr

            l += 1
            r += 1

        return ans / k


# Time complexity : O(n)
# Space complexity : O(1)

if __name__ == '__main__':
    print(Solution.findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))
