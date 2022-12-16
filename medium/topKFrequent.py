"""
https://leetcode.com/problems/top-k-frequent-elements/
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
"""
from typing import List
from collections import Counter


class Solution:
    @staticmethod
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)

        return [i[0] for i in nums.most_common(k)]

# Time Complexity: O(Nlog(k))
# Space Complexity: O(N+k)


if __name__ == '__main__':
    print(Solution.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))  # [1, 2]
