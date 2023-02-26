"""
https://leetcode.com/problems/number-of-good-pairs/
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.


Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:
Input: nums = [1,2,3]
Output: 0
 
Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""
from itertools import product, permutations, combinations
from collections import Counter
from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_counter = Counter(nums)
        return int(sum( val * (val - 1) / 2 for val in num_counter.values()))
    

print(Solution().numIdenticalPairs([1,2,3,1,1,3]))
    
print(list(product('1234')))
for e in combinations('12345', 2):
    print(''.join(e), end=", ")