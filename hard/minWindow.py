"""
https://leetcode.com/problems/minimum-window-substring/
Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.
s and t consist of uppercase and lowercase English letters.
"""


class Solution:
    @staticmethod
    def minWindow(s: str, t: str) -> str:
        if t == "":
            return ""

        count_t, window = {}, {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float('inf')
        left = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in count_t and window[c] == count_t[c]:
                have += 1

            while have == need:
                # update result
                if (r - left + 1) < res_len:
                    res = [left, r]
                    res_len = r - left + 1
                # pop from the left of window
                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1
        left, r = res
        return s[left: r + 1] if res_len != float('inf') else ""


if __name__ == '__main__':
    print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"))  # "BANC"

# Time Complexity: O()
# Memory Complexity: O()
