"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = curr_count_zero = left = 0
        for idx, val in enumerate(nums):
            if val == 0:
                curr_count_zero += 1
            if curr_count_zero > k:
                curr_count_zero = curr_count_zero - 1 if nums[left] == 0 else curr_count_zero
                left += 1
                
            max_len = max(max_len, idx - left + 1)
            
        return max_len
                
            
            
