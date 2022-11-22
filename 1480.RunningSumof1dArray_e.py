"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
"""
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Beats 91.41% 
        result = []
        pre_sum = 0
        num_len = len(nums)
        #for idx, val in enumerate(nums):
        for idx in range(num_len):
            if idx == 0:
                result.append(nums[idx])
                pre_sum = nums[idx]
            else:
                pre_sum = pre_sum + nums[idx]
                result.append(pre_sum)
        return result
    
    
    def runningSum2(self, nums: List[int]) -> List[int]:
        # 
        for idx in range(1, len(nums)):
            nums[idx] += nums[idx - 1]
            
        return nums