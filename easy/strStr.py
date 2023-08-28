"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        m = len(needle)
        n = len(haystack)

        for window_start in range(n - m + 1):
            for i in range(m):
                if needle[i] != haystack[window_start + i]:
                    break
                if i == m - 1:
                    return window_start
        
        return -1
    
    # Time Complexity: O(n*m)
    # Memory Complexity: O(1)

if __name__ == "__main__":
    print(Solution().strStr(haystack="hello", needle="ll"))  # 2