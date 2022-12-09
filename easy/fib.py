"""
https://leetcode.com/problems/fibonacci-number/
The Fibonacci numbers, commonly denoted F(n) form a sequence,
called the Fibonacci sequence, such that each number is the sum of the two preceding ones,
starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).
"""


class Solution:
    @staticmethod
    def fib_recursive(n: int) -> int:
        # Recursive approach
        # Time complexity : O(2^n)
        # Space complexity : O(n)
        if n <= 1:
            return n
        return Solution.fib_recursive(n - 1) + Solution.fib_recursive(n - 2)


    @staticmethod
    def fib_iterative(n: int) -> int:
        # Iterative approach
        # Time complexity : O(n)
        # Space complexity : O(1)
        prev, curr = 0, 1
        while n > 0:
            prev, curr = curr, prev + curr
            n -= 1
        return prev
