"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
from typing import List
import numpy as np

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        faster than 5.21%
        """
        default_ans = [-1, -1]
        if not nums: return default_ans
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return default_ans

        nums = np.array(nums)
        ans = np.where(nums == target)[0]
        if len(ans) < 1:
            return default_ans
        elif len(ans) == 1:
            return [ans[0], ans[0]]
        else:
            return [ans[0], ans[-1]]

    def searchRangeImporve(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        if not nums: return [-1, -1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] > target:
                return [-1, -1]

            if ans[0] == -1:
                if nums[left] == target:
                    ans[0] = left
                else:
                    left += 1
            if ans[1] == -1:
                if nums[right] == target:
                    ans[1] = right
                else:
                    right -= 1

            if ans[0] != -1 and ans[1] != -1:
                return ans

        if -1 in ans:
            return [-1, -1]
        else:
            return ans

    def searchRangeSolution(self, nums, target):
        """
        faster than 83.82%
        Time complexity : O(n)
        Space complexity : O(1)
        """
        # find the index of the leftmost appearance of `target`. if it does not
        # appear, return [-1, -1] early.
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        # find the index of the rightmost appearance of `target` (by reverse
        # iteration). it is guaranteed to appear.
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx, right_idx]

    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def searchRangeBinarySearch(self, nums, target):
        """
        Time complexity : O(log N)
        Space complexity : O(1)
        """
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False) - 1]


if __name__ == "__main__":
    testcases = [
        {'s': [5, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 10], 't': 8, 'e': [3, 10]},
        {'s': [5, 7, 7, 8, 8, 10], 't': 6, 'e': [-1, -1]},
        {'s': [1, 3], 't': 1, 'e': [0, 0]},
    ]
    for case in testcases:
        actual_result = Solution().searchRangeBinarySearch(case['s'], case['t'])
        print("Input: {}\nExpected: {}\nAcutal: {}\nis_Passed: {}".format(case['s'],
                                                                          case['e'],
                                                                          actual_result,
                                                                          actual_result == case['e']))
