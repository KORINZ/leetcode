"""
https://leetcode.com/problems/product-of-array-except-self/
Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)
"""
from typing import List


class Solution:
    @staticmethod
    def productExceptSelf(nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in reversed(range(len(nums))):
            ans[i] *= postfix
            postfix *= nums[i]

        return ans


# Time complexity : O(N)
# Space complexity : O(1)

if __name__ == '__main__':
    print(Solution.productExceptSelf(nums=[1, 2, 3, 4]))  # [24,12,8,6]
