"""
House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

Example 3:
Input: [2,1,1,2]
Output: [4]
"""
from typing import List

class Solution:
    """
    let us denote:
    f(k) = largest amount that you can rob from the first K houses.
    Ai = Amount of money at the i^th house
    when n = 1, f(1) = A
    when n = 2, f(2) = max(A1, A2)
    when n = 3:
    1. Rob the third house, and adds its amount to the first house's amount
    2. Do not rob the third house, and stick with the maximum amount of the first two houses. max(A1, A2).
    we could summarize the formula:
    f(k) = max(f(k-2) + A[k], f(k -1))

    """
    def rob(self, nums: List[int]) -> int:
        prev_max = curr_max = 0
        for i in range(len(nums)):
            temp = curr_max
            curr_max = max(prev_max + nums[i], curr_max)
            prev_max = temp

        return curr_max


if __name__ == "__main__":
    nums = [2,1,1,2]
    print(Solution().rob(nums))
