"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers(奇数也说单数，不能被2整除) on it.

Return the number of nice sub-arrays.


Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.

Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 
Constraints:
1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
"""
from collections import defaultdict
from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0
        
        for num in nums:
            curr += num % 2
            minus = curr - k
            ans += counts[minus]
            counts[curr] += 1

        return ans
    
    
nums = [2,2,2,1,2,2,1,2,2,2]
print(Solution().numberOfSubarrays(nums, 2))