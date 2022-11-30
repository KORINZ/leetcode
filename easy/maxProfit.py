"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
from typing import List


class Solution:
    @staticmethod
    def maxProfit(prices: List[int]) -> int:  # NOQA
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                if profit > max_profit:
                    max_profit = profit
                r += 1
            else:
                l = r
                r += 1
        return max_profit


if __name__ == '__main__':
    print(Solution().maxProfit([1, 9, 0, 9]))

# Time Complexity: O(n)
# Memory Complexity: O(1)
