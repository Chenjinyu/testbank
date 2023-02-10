"""
You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums.

Example 1:
Input: nums = [10,4,-8,7]
Output: 2
Explanation: 
There are three ways of splitting nums into two non-empty parts:
- Split nums at index 0. Then, the first part is [10], and its sum is 10. The second part is [4,-8,7], and its sum is 3. Since 10 >= 3, i = 0 is a valid split.
- Split nums at index 1. Then, the first part is [10,4], and its sum is 14. The second part is [-8,7], and its sum is -1. Since 14 >= -1, i = 1 is a valid split.
- Split nums at index 2. Then, the first part is [10,4,-8], and its sum is 6. The second part is [7], and its sum is 7. Since 6 < 7, i = 2 is not a valid split.
Thus, the number of valid splits in nums is 2.

Example 2:
Input: nums = [2,3,1,0]
Output: 2
Explanation: 
There are two valid splits in nums:
- Split nums at index 1. Then, the first part is [2,3], and its sum is 5. The second part is [1,0], and its sum is 1. Since 5 >= 1, i = 1 is a valid split. 
- Split nums at index 2. Then, the first part is [2,3,1], and its sum is 6. The second part is [0], and its sum is 0. Since 6 >= 0, i = 2 is a valid split.

Constraints:
2 <= nums.length <= 105
-105 <= nums[i] <= 105
"""

from typing import List
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        """ Time Limit Exceeded due to 3 for loop with large nums of list """
        nums_len = len(nums)
        prefix_sum = [nums[0]]
        back_prefix_sum = [nums[-1]]
        ans = 0
        for n in range(1, nums_len):
            prefix_sum.append(nums[n] + prefix_sum[-1])
        
        for m in range(nums_len - 2, -1, -1):
            back_prefix_sum.insert(0, (nums[m] + back_prefix_sum[0]))

        for idx in range(0, nums_len - 1):
            if prefix_sum[idx] >= back_prefix_sum[idx + 1]:
                ans += 1
        
        return ans
            
            
    def waysToSplitArray2(self, nums: List[int]) -> int:
        """ 
        eg:
        nums = [10, 4, -8, 7] -> prefix_sum = [10, 14, 6, 13]
        so, the 13 is the sum of nums, 13(nums[-1]) - 10(nums[0]) is the rest of item[4, -8, 7]
        13 - 14 (sum of [10, 4]) is sum of [-8, 7]
        """
        prefix_sum = [nums[0]]
        nums_len = len(nums)
        ans = 0
        for n in range(1, nums_len):
            prefix_sum.append(nums[n] + prefix_sum[-1])
        
        for idx in range(nums_len - 1):
            left_section = prefix_sum[idx]
            right_section = prefix_sum[-1] - prefix_sum[idx]
            if left_section >= right_section:
                ans += 1
                
        return ans        
        
            