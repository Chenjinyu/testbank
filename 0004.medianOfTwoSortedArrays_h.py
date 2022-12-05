"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

from typing import List
import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if(len(nums1) > len(nums2)):
            return Solution().findMedianSortedArrays(nums2, nums1)
        num1_len, num2_len = len(nums1), len(nums2)
        
        low = 0
        high = num1_len
        
        while(low <= high):
            partition_x = math.floor(low + high / 2)
            partition_y = math.floor((num1_len + num2_len + 1) / 2) - partition_x # make sure the items in the 2L halfs almost equals the 2R halfs
            
            max_left_x = -math.inf if partition_x == 0 else nums1[partition_x - 1]
            min_right_x = math.inf if partition_x == num1_len else nums1[partition_x]
            
            max_left_y = -math.inf if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = math.inf if partition_y == num2_len else nums2[partition_y]
            
            if(max_left_x <= min_right_y and min_right_x >= max_left_y):
                if((num1_len + num2_len) % 2 == 0):
                    return float(max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                else:
                    return float(max(max_left_x, max_left_y)) / 2
            elif (max_left_x > min_right_y):
                high = partition_x - 1
            else:
                low = partition_x + 1
        
        
        
        