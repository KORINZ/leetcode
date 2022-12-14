"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
"""
from typing import List


class Solution:
    @staticmethod
    def maxProfit(prices: List[int]) -> int:

        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]


if __name__ == '__main__':
    pass
