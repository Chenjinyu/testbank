"""
Google and Amazon OA

Given an unsorted array of integers, find the length of longest increasing sub-sequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing sub-sequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""
class Solution:
    def longestIncreaseSubsequenceDP(nums):
    """
    Time Complexity: O(N^2)
    Space Complexity: O(N)
    """
    if not nums: return 0
    # set dp list default as 1. coz, only has it self will return 1.
    dp = [1] * len(nums)
    # 这道题无法避免的需要两次loop。从nums的第一个开始，查看它之前是否有小于它的数
    # 如果有，就求出 dp[i] = max(dp[i], dp[j] + 1)
    # 比如：当i 为3时，dp[i] = max(dp[i], dp[1]的值 + 1) 和 dp[i] = max(dp[i], dp[2]的值 + 1), 取其最大值。
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

if __name__ == "__main__":
    testcases = [
        {'nums': [1, 5, 3, 4, 6, 9, 7, 8], 'e': 6},
        {'nums': [6, 5, 3, 4, 6, 9, 7, 8], 'e': 5},
    ]
    for case in testcases:
        actual_result = longestIncreaseSubsequenceDP(case['nums'])
        print("Input: {}\nExpected: {}\nAcutal: {}\nis_Passed: {}".format(case['nums'],case['e'], actual_result, actual_result== case['e']))
