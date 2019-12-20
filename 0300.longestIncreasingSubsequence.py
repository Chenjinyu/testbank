"""
Google and Amazon OA

Given an unsorted array of integers, find the length of longest increasing sub-sequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing sub-sequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        left, right = 0, 1
        count = 0
        while right < len(nums):
            if nums[left] < nums[right]:
                right += 1
                count += 1
            else:
                left += 1
                right += 1
        return count


if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    print(Solution().lengthOfLIS(nums))