"""
https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4595/
Given a binary array nums and an integer k,
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""
from typing import List


class Solution:
    @staticmethod
    def longestOnes(nums: List[int], k: int) -> int:
        l = 0
        counter = 0
        longest = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                counter += 1

            if counter > k:
                while counter != k:
                    if nums[l] == 0:
                        counter -= 1
                    l += 1

            if longest < r - l + 1:
                longest = r - l + 1

        return longest


# Time Complexity: O(N)
# Space Complexity: O(1)

if __name__ == '__main__':
    print(Solution.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))  # 6
