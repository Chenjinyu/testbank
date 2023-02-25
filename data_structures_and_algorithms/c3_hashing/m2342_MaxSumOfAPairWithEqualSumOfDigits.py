"""
You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.


Example 1:
Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.

Example 2:
Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.
 
Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 109
"""

from typing import List
from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dct = defaultdict(int)
        ans = float('-inf')
        for num in nums:
            digit_count = self.getSumofDigits(num)
            if digit_count in dct.keys():
                ans = max(ans, dct[digit_count] + num)
            dct[digit_count] = max(dct[digit_count], num)
            
        return ans if ans > float('-inf') else -1
    
    def get_digit_sum(self, num):
            digit_sum = 0
            while num:
                digit_sum += num % 10
                num //= 10
            
            return digit_sum
        
    def getSumofDigits(self, num: int) -> int:
        ans = 0
        while num:
            num, tmp = divmod(num, 10)
            ans += tmp
            
        return ans
    
    def getSumofDigitsByStr(self, num: int) -> int:
        ans = 0
        num_str = str(num)
        for i in range(len(num_str)):
            ans += int(num_str[i])
        return ans
    
    
        
nums = [279,169,463,252,94,455,423,315,288,64,494,337,409,283,283,477,248,8,89,166,188,186,128]
print(Solution().maximumSum(nums = [279,169,463,252,94,455,423,315,288,64,494,337,409,283,283,477,248,8,89,166,188,186,128]
))
        
    