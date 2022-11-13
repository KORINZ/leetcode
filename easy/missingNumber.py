"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
"""
from typing import List


class Solution:
    @staticmethod
    def missingNumber(nums: List[int]) -> int:
        result = len(nums)
        for i in range(0, len(nums)):
            diff = i - nums[i]
            result += diff
        return result


if __name__ == '__main__':
    print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8

# Time Complexity: O(n)
# Memory Complexity: O(1)
