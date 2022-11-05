# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

class Solution:
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        s_letters = [letter for letter in s].sort()
        t_letters = [letter for letter in t].sort()
        if s_letters == t_letters:
            return True
        else:
            return False

    # Time Complexity: O(nlog(n))
    # Memory Complexity: O(n)

    # TODO Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

    @staticmethod
    def unicode_isAnagram(s: str, t: str) -> bool:
        pass


if __name__ == '__main__':
    print(Solution().isAnagram(s='listen', t='silent'))  # True
