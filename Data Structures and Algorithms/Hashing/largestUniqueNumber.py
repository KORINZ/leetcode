"""
https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4662/
Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.
"""
from typing import List
from collections import Counter


class Solution:
    @staticmethod
    def largestUniqueNumber(nums: List[int]) -> int:
        count_dict = Counter(nums)
        ans = set()
        for key in count_dict:
            if count_dict[key] == 1:
                ans.add(key)

        return max(ans) if ans else -1


# Time complexity : O(n)
# Space complexity : O(n)

if __name__ == '__main__':
    print(Solution.largestUniqueNumber(nums=[5, 7, 3, 9, 4, 9, 8, 3, 1]))  # 8
