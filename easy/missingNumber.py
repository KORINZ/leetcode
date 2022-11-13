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

    # Time Complexity: O(n)
    # Memory Complexity: O(1)

    @staticmethod
    def missingNumberWay2(nums: List[int]) -> int:
        full_list = list(range(0, len(nums) + 1))
        for number in full_list:
            if number not in nums:
                return number
    # Time Complexity: O(n)
    # Memory Complexity: O(n)


if __name__ == '__main__':
    question_input = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(Solution().missingNumber(question_input))  # 8
    print(Solution().missingNumberWay2(question_input))  # 8
