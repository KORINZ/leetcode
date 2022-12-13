"""
https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4607/
Given two strings ransomNote and magazine,
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""
from collections import Counter


class Solution:
    @staticmethod
    def canConstruct(ransom_note: str, magazine: str) -> bool:
        ransom_note = Counter(ransom_note)
        magazine = Counter(magazine)

        for key in ransom_note:
            if ransom_note[key] > magazine[key]:
                return False

        return True


# Time complexity : O(m) where m = len(magazine)
# Space complexity : O(1)

if __name__ == '__main__':
    print(Solution.canConstruct(ransom_note="aa", magazine="aab"))  # True
