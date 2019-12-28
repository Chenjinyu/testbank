"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

Algorithm: [A]
∑ n    i = n (n + 1) / 2    
  i=0  	
  
  
Note:
Think about if the number does not start with 0, but it's n= [k, k + 1, K+ 2, ... k + m]. and it has a long items.
one of my solutions is:
1. sort them.
2. find the mid_pos, if the nums[mid_pos] > k + (k + m) / 2, the missing number should be the left side, vice versa.

could we use the algorithm [A]? I think it will be more efficience. 

Algorithm: [A]
∑ n    i = n (n + 1) / 2
  i=0

"""
from typing import List


class Solution:
    """
    Amazon OA Problem
    Microsoft OA Problem
    """
    def missingNumber(self, nums: List[int]) -> int:
        """
        We can compute the sum of nums in linear time, and by Gauss' formula, 
        we can compute the sum of the first N natural numbers in constant time. 
        Therefore, the number that is missing is simply the result of Gauss' formula minus the sum of nums, 
        as nums consists of the first nn natural numbers minus some number.
        """
        # aims to return integer not float. coz it could not be a float. eg 1.23
        # the algorithm of len(nums) * (len(nums) + 1) // 2, only uses for the number starts from 0.
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

    def missingNumberBySet(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number
                

    def missingNumberByBit(self, nums):
        """
        Approach #3 Bit Manipulation [Accepted]
        """
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
        
if __name__ == "__main__":
    nums = [9,6,4,2,3,5,7,0,1]
    print(Solution().missingNumber(nums))
