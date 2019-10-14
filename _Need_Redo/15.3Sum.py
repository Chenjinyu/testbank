"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

idea: sort the list, and get the zero point. sliding down from left to right. right to left.
after sort, easy to check the duplicated value, and skip them.
so that don't need to use dict{} to avoid duplicate list has been added in.

"""
from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))