"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
"""
from typing import List


# Approach 1: Sort
# sorted(x * x for x in nums)
# Time Complexity: O(NlogN), where N is the length of nums.
# Space complexity : O(N) b.c. Timsort.


# Approach 2: Two Pointer
class Solution:
    @staticmethod
    def sortedSquares(nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left, right, square = 0, n - 1, 0

        for i in reversed(range(n)):
            if abs(nums[left]) > abs(nums[right]):
                square = nums[left]
                left += 1
            else:
                square = nums[right]
                right -= 1

            res[i] = square ** 2

        return res


# Time Complexity: O(N), where N is the length of A.
# Space Complexity: O(N)

if __name__ == '__main__':
    print(Solution.sortedSquares(nums=[-4, -1, 0, 3, 10]))  # [0, 1, 9, 16, 100]
