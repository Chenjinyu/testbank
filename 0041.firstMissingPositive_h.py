"""
41. First Missing Positive
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1
Note:
Your algorithm should run in O(n) time and uses constant extra space.
"""
from typing import List


class Solution:
    """
    Google OA Problem
    Amazon OA Problem
    Facebook OA Problem
    Apple OA Problem
    Databricks OA Problem
    Bloomberg OA Problem
    Wish OA Problem
    ByteDance OA Problem
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        # sorted(nums) # time complexity: O(N log N)
        if not nums:
            return 1

        nums.sort()
        for i in range(1, (len(nums) + 2)):
            if not nums.count(i):
                return i


if __name__ == "__main__":
    testcases = [
        {'nums': [1, 2, 0], 'e': 3},
        {'nums': [1, 2, 3, 4, 5, 6, 7, 8], 'e': 9},
        {'nums': [1, 2, 48, 14, 15, 16, 17, 18], 'e': 3},
        {'nums': [1, 2, 3, 4, 5, 6, 7, 18], 'e': 8},
        {'nums': [3, 4, -1, 1], 'e': 2},
        {'nums': [7, 8, 9, 11, 12], 'e': 1},
        {'nums': [1, 8, 9, 11, 12], 'e': 2},
    ]
    for case in testcases:
        actual_result = Solution().firstMissingPositive(case['nums'])
        print("Input: {}\nExpected: {}\nAcutal: {}\nis_Passed: {}".format(case['nums'],
                                                                          case['e'],
                                                                          actual_result,
                                                                          actual_result == case['e']))