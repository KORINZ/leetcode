"""
https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4663/
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
"""
from collections import Counter


class Solution:
    @staticmethod
    def maxNumberOfBalloons(text: str) -> int:
        text_dict = Counter(text)

        return min(text_dict["b"], text_dict["a"], text_dict["l"] // 2, text_dict["o"] // 2, text_dict["n"])


# Time complexity : O(n)
# Space complexity : O(1)

if __name__ == '__main__':
    print(Solution.maxNumberOfBalloons(text="loonbalxballpoon"))  # 2
