# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

from typing import List


class Solution:
    @staticmethod
    def search(nums: List[int], target: int) -> int:
        def recursive_binary_search(start, end):

            mid_index = start + ((end - start) // 2)

            if start > end:
                return -1
            elif target == nums[mid_index]:
                return mid_index
            elif target < nums[mid_index]:
                return recursive_binary_search(start, mid_index - 1)
            elif target > nums[mid_index]:
                return recursive_binary_search(mid_index + 1, end)

        return recursive_binary_search(start=0, end=len(nums) - 1)


if __name__ == '__main__':
    print(Solution().search(nums=[2, 7, 11, 15, 28, 99, 101], target=11))  # return 2 since target=11 -> nums[2]

# Time Complexity: O(log(n))
# Memory Complexity: O(1)
