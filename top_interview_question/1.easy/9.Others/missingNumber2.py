"""
the question added by myself.

Note:
Think about if the number does not start with 0, but it's n= [k, k + 1, K+ 2, ... k + m]. and it has a long items.
one of my solutions is:
1. sort them.
2. find the mid_pos, if the nums[mid_pos] > k + (k + m) / 2, the missing number should be the left side, vice versa.

Could we use the algorithm [A]? I think it will be more efficience.


Given an array containing n distinct numbers taken from n, n+1, n+2, ..., m, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9, 6, 4, 5, 7, 10, 11, 12, 13]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

Algorithm: [A]
∑ n    i = n (n + 1) / 2
  i=0



"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # // aims to return integer not float. coz it could not be a float. eg 1.23
        min_num = min(nums)
        supplement_nums = [x for x in range(min_num)]
        nums = supplement_nums + nums
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


if __name__ == "__main__":
    nums = [9, 6, 4, 5, 7, 10, 11, 12, 13]
    print(Solution().missingNumber(nums))
