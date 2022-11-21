"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""
from typing import List


class Solution:
    @staticmethod
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        pass


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [["bat"],["nat","tan"],["ate","eat","tea"]]

# Time Complexity: O()
# Memory Complexity: O()
