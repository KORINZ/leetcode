"""
https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4602/
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
"""
from typing import List


class Solution:
    @staticmethod
    def missingNumber(nums: List[int]) -> int:
        nums_set = set(nums)

        for i in range(len(nums) + 1):
            if i not in nums_set:
                return i


# Time complexity : O(n)
# Space complexity : O(n)

if __name__ == '__main__':
    print(Solution.missingNumber(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8 b.c. 8 is missing
