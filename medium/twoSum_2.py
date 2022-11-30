"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.
"""
from typing import List


class Solution:
    @staticmethod
    def twoSum_2(numbers: List[int], target: int) -> List[int]:  # NOQA
        l, r = 0, len(numbers) - 1

        for i in range(len(numbers)):
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l + 1, r + 1]


if __name__ == '__main__':
    print(Solution().twoSum_2(numbers=[2, 7, 11, 15],
                              target=26))  # [3, 4] since 11+15=26 (index starts from 1 instead of 0)

# Time Complexity: O(n)
# Memory Complexity: O(1)
