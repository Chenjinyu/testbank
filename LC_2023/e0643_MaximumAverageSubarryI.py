"""
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

Constraints:

* n == nums.length
* 1 <= k <= n <= 105
* -104 <= nums[i] <= 104
"""
from typing import List
class Solution:
    def findMaxAverageFaildDueToWithoutMaxVarReturns(self, nums: List[int], k: int) -> float:
        """ Should not use current value to present max value """
        curr = 0
        # curr = sum(nums[:k])
        # inital curr val at beginning
        for i in range(k):
            curr += nums[i]
        
        for j in range(k, len(nums)):
            # the curr value is not the curr value instead of the max value.
            # so, its worng.
            tmp = curr + nums[j] - nums[j - k]
            curr = max(curr, tmp)
        
        return round(curr/k, 5)
    
    
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])
        max_curr = curr
 
        for j in range(k, len(nums)):
            curr += nums[j] - nums[j - k]
            max_curr = max(curr, max_curr)
        
        return round(max_curr/k, 5)
