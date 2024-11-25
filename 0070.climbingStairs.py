"""
Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Solution:
    #
    def climbStairsFib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 1, 2
        for i in range(3, n + 1):
            sums = a + b
            a = b
            b = sums
        return b

    # dynamic programming, the big problem is how can i find
    # a solution and how to use dp.
    def climbStairsDP(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [1, 2]
        for i in range(3, n + 1):
            dp[0], dp[1] = dp[1], dp[0] + dp[1]
        return dp[i]

    def climbStairsIteration(self, n: int) -> int:
        # has Time Limit Execeeded issue
        def recursionClimb(step, n):
            if step > n:
                return 0
            if step == n:
                return 1
            return recursionClimb(step + 1, n) + recursionClimb(step + 2, n)

        return recursionClimb(0, n)


if __name__ == "__main__":
    n = 3
    print(Solution().climbStairsFib(n))
