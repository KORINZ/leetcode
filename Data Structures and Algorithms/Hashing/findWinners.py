"""
https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4606/
You are given an integer array matches where matches[i] = [winner_i, loser_i]
indicates that the player winner_i defeated player loser_i in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
"""
from typing import List
from collections import Counter


class Solution:
    @staticmethod
    def findWinners(matches: List[List[int]]) -> List[List[int]]:
        winner_set = set(i[0] for i in matches)
        loser_dict = Counter(i[1] for i in matches)

        ans_0 = [key for key in winner_set if key not in loser_dict]
        ans_1 = [key for key in loser_dict if loser_dict[key] == 1]

        ans_0.sort()
        ans_1.sort()
        return [ans_0, ans_1]


# Time complexity : O(nlog(n))
# Space complexity : O(n)

if __name__ == '__main__':
    print(Solution.findWinners(
        matches=[[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))

    # [[1,2,10],[4,5,7,8]]

    # Explanation:
    # Players 1, 2, and 10 have not lost any matches.
    # Players 4, 5, 7, and 8 each have lost one match.
    # Players 3, 6, and 9 each have lost two matches.
    # Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
