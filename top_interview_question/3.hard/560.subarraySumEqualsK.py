"""
560. Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        length = len(nums)
        if length == 0:
            return 0
        if length == 1 and nums[0] == k:
            return k

        left = right = 0
        equal_sum_num = 0

        while right <= length:
            sub_sum = sum(nums[left:right])
            if sub_sum < k:
                right += 1
            elif sub_sum > k:
                left += 1
            else:  # sub_sum equals k
                equal_sum_num += 1


if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(Solution().subarraySum(nums, k))