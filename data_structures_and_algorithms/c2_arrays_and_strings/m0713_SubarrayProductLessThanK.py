"""
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

Example 1:
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:
Input: nums = [1,2,3], k = 0
Output: 0

Constraints:
- 1 <= nums.length <= 3 * 104
- 1 <= nums[i] <= 1000
- 0 <= k <= 106
"""
from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """ Time Limit Exceeded due to the right euqals left line27
        because it forces the step back"""
        ans = 0
        for left in range(len(nums)):
            right = left
            curr = nums[left]
            while curr < k:
                ans += 1
                right += 1
                if right <= len(nums) - 1:
                    curr = nums[right] * curr
                else:
                    break
            
        return ans
    
    
    def numSubarrayProductLessThanK2(self, nums: List[int], k: int) -> int:
        """ Since the length of subarray is the mount of combination subarraies which product less than K  """
        if k <= 1: return 0
        curr = 1
        ans = left = 0
        for right, val in enumerate(nums):
            curr *= val
            while curr >= k:
                curr /= nums[left]
                left +=1
            ans += right - left + 1 # how many items in a specifix index started subarray is how many subarray which product less than k.
        return ans
                