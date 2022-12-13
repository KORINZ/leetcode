"""
https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4690/
Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        ans = 0

        # store index values of char
        char_dict = dict()

        left = 0
        for right in range(len(s)):
            if s[right] in char_dict:
                left = max(char_dict[s[right]], left)

            ans = max(ans, right - left + 1)
            char_dict[s[right]] = right + 1

        return ans

    # Sliding Window Optimized
    # Time complexity : O(n)
    # Space complexity : O(min(m,n))


if __name__ == '__main__':
    print(Solution.lengthOfLongestSubstring(s="pwwkew"))  # 3
    # Explanation: The answer is "wke", with the length of 3.
    # Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
