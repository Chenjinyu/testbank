"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:
Input: coins = [2], amount = 3
Output: -1
Example: 3
Input: coins = [186, 419, 83, 408], amount = 6249
Output: 20
"""


class Solution:
    def coinChange(self, coins, amount):
        """
        dynamic programming solution
        dp[i]: minimal number of coins to make i cents
        transfer function dp[i] = min(dp[i], dp[i - coin] + 1 if i >= coin)
        i = 11, coin = 5, dp[i],  dp[11 - 5] + 1(5 cents) = dp[6] + 1
        i = 11, coin = 2, dp[i],  dp[11 - 2] + 1(5 cents) = dp[9] + 1
        i = 11, coin = 1, dp[i],  dp[11 - 1] + 1(5 cents) = dp[10] + 1
        # dp[0] = 0
        """
        INF = float('inf')
        dp = [0] + [INF] * amount
        for i in range(amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != INF else -1

    def coinChangeDSF(self, coins, amount):
        coins = sorted(coins)[::-1]
        min_number = float('inf')

        min_number = self.change_helper(coins, 0, amount, 0, min_number)
        return -1 if min_number == float('inf') else min_number

    def change_helper(self, coins, start_pos, amount, count, min_number):
        coin = coins[start_pos]
        # last element, eg: 1.
        if start_pos == len(coins) - 1:
            if amount % coin == 0:
                min_number = min(min_number, (count + amount // coin))
        else:
            k = amount // coin
            # count is current count of coins which be included in.
            # count + k must less than min_number, otherwise, it's not the optimal answer.
            if k >= 0 and count + k < min_number:
                for i in range(k, -1, -1):
                    min_number = self.change_helper(coins, start_pos + 1, (amount - i * coin), (count + i), min_number)
        return min_number

    def coinChangeDSFImprove(self, coins, amount):
        """
        has issue, min_number is None
        solution: back-tracking.
        the root cause is the coins list will be used multiple times.
        """
        coins.sort()  # coins = sorted(coins)
        min_number = float('inf')
        min_number = self.change_helper_improve(coins, amount, 0, min_number)
        return -1 if min_number == float('inf') else min_number

    def change_helper_improve(self, coins, amount, count, min_number):
        if len(coins):
            coin = coins.pop()
            k = amount // coin
            if len(coins) == 0:
                if amount % coin == 0:
                    min_number = min(min_number, k + count)
            else:
                if k >= 0 and count + k < min_number:
                    for i in range(k, -1, -1):
                        min_number = self.change_helper_improve(coins, amount - i * coin, count + i, min_number)

            return min_number



if __name__ == "__main__":
    # coins_list = [186, 419, 83, 408]
    # amount = 6249
    coins_list = [1, 2, 5]
    amount_expected = 11
    print(Solution().coinChangeDSFImprove(coins_list, amount_expected))