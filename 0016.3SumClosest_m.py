"""
16. 3Sum Closest

Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

from typing import List

class Solution:
    """
    Google OA Problem
    Amazon OA Problem
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums:
            return []
        nums.sort()

        closest_num = float('inf')

        num_len = len(nums)
        # range(num_len - 1) is much faster than range(len(nums) - 1)
        for idx in range(num_len - 1):
            left, right = idx + 1, len(nums) - 1
            while left < right:
                three_sum = nums[idx] + nums[left] + nums[right]
                if abs(target - closest_num) > abs(target - three_sum):
                    closest_num = three_sum
                if three_sum < target:
                    left += 1
                elif three_sum > target:
                    right -= 1
                else:
                    return three_sum

        return closest_num


if __name__ == "__main__":
    testcases = [
        {'s': [-1, 2, 1, -4], 't': 1, 'e': 2},
        {'s': [0, 0, 0], 't': 1, 'e': 0},
    ]
    is_pass = True
    for case in testcases:
        actual_result = Solution().threeSumClosest(case['s'],case['t'])
        print("Expected: {}\nAcutal: {}\nis_Passed: {}".format(case['e'],
                                                               actual_result,
                                                               actual_result == case['e']))
        if actual_result != case['e']:
            is_pass = False

    if not is_pass:
        print("!!!!-----FAILED------!!!!")
