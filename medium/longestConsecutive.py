"""
https://leetcode.com/problems/longest-consecutive-sequence/
Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""
from typing import List


class Solution:
    @staticmethod
    def longestConsecutive(nums: List[int]) -> int:  # NOQA
        nums_set = set(nums)
        longest_seq = 0

        for n in nums:
            if n - 1 not in nums_set:
                length_seq = 0
                while n + length_seq in nums_set:
                    length_seq += 1
                longest_seq = max(length_seq, longest_seq)
        return longest_seq


if __name__ == '__main__':
    print(Solution().longestConsecutive([0, 1, 2, 3, 100, 300]))  # 4

# Time Complexity: O(n)
# Memory Complexity: O(n)
