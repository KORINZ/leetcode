"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Constraint:
1 <= n <= 45
"""


class Solution:
    @staticmethod
    def climbStairs(n: int) -> int:  # NOQA
        pass


if __name__ == '__main__':
    print(Solution().climbStairs(n=3))  # 3
    # There are three ways to climb to the top.
    # 1. 1 step + 1 step + 1 step
    # 2. 1 step + 2 steps
    # 3. 2 steps + 1 step

# Time Complexity: O()
# Memory Complexity: O()
