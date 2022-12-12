"""
https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4661/
Given an integer array arr, count how many elements x there are,
such that x + 1 is also in arr. If there are duplicates in arr, count them separately.
"""
from typing import List


class Solution:
    @staticmethod
    def countElements(arr: List[int]) -> int:
        nums_set = set(arr)
        count = 0

        for n in arr:
            if n + 1 in nums_set:
                count += 1

        return count


# Time complexity : O(n)
# Space complexity : O(n)

if __name__ == '__main__':
    print(Solution.countElements(arr=[1, 2, 3]))  # 2 b.c. 1 and 2 are counted cause 2 and 3 are in arr
