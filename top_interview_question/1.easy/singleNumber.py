"""
Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4

Soluton: Counter.
"""
from collections import Counter

class Solution:
    def singleNumber(self, nums: list):
        num_counter = Counter(nums)
        for k, v in num_counter.items():
            if v == 1:
                return k

if __name__ == "__main__":
    nums = [4,1,2,1,2]
    print(Solution().singleNumber(nums))

