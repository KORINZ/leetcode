"""
https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4601/
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters,
return true if sentence is a pangram, or false otherwise.
"""


class Solution:
    @staticmethod
    def checkIfPangram(sentence: str) -> bool:
        sentence = set(sentence)

        return len(sentence) == 26


# Time complexity : O(n)
# Space complexity : O(1)

if __name__ == '__main__':
    print(Solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))  # True
