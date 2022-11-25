"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""
from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)

        for word in strs:
            count = [0] * 26  # a, b, c, ..., z (all start with 0)
            for char in word:
                count[ord(char) - ord("a")] += 1  # ord("a") = 97
            results[tuple(count)].append(word)
        return list(results.values())


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [["bat"],["nat","tan"],["ate","eat","tea"]]

# Time Complexity: O(m*n)
# Memory Complexity: O(m*n)
