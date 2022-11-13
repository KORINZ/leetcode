"""
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""
from typing import List


class Solution:
    @staticmethod
    def canJump(nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):  # starting from goal to the beginning
            if i + nums[i] >= goal:
                goal = i

        if goal == 0:  # check if goal can reach index 0
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().canJump(nums=[2, 5, 0, 0]))  # True since 2 -> 5 -> goal

# Time Complexity: O(n)
# Memory Complexity: O(1)
