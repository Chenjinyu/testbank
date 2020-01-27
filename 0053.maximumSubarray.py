"""
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle.
"""

from typing import List
from itertools import accumulate

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prefix_sums_list = list(accumulate(nums))
        print(prefix_sums_list)
        return max(prefix_sums_list) - min(prefix_sums_list)

    def maxSubArrayImprove(self, nums: List[int]) -> int:
        length = len(nums)
        # consider when length of list equals 1.
        cur_sum = max_sum = nums[0]
        # starts from pos = 1, because pos 0 already taken.
        for i in range(1, length):
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(cur_sum, max_sum)
        return max_sum


if __name__ == "__main__":
    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    # nums = [-2,1]
    nums = [-2, -1]
    print(Solution().maxSubArrayImprove(nums))