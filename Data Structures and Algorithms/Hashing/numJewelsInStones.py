"""
https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4664/
You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have.
Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case-sensitive, so "a" is considered a different type of stone from "A".
"""


class Solution:
    @staticmethod
    def numJewelsInStones(jewels: str, stones: str) -> int:
        jewels = set(jewels)

        ans = sum(i in jewels for i in stones)  # the generator represents boolean values

        return ans


# Time complexity : O(m+n)
# Space complexity : O(1) (when not considering the input)

if __name__ == '__main__':
    print(Solution.numJewelsInStones(jewels="aA", stones="aAAbbbb"))  # 3
