"""
Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos_list = []
        start = 0
        while start < len(nums):
            result_item = target - nums[start]
            if result_item in nums:
                result_item_index = nums.index(result_item)
                if result_item_index != start:
                    pos_list.extend([start, result_item_index])
                    nums.remove(nums[start])
                    nums.remove(result_item)
                else:
                    start += 1
            else:
                start += 1
        return pos_list
    
    """
    Amazon OA Problem.
    """
    def twoSumRedo(self, nums: List[int], target: int) -> List[int]:
        for idx in range(len(nums)):
            result = target - nums[idx]
            if result in nums:
                result_idx = nums.index(result)
                if result_idx != idx:
                    return [idx, result_idx]


if __name__ == "__main__":
    nums1 = [2, 11, 15, 7]
    target = 9
    print(Solution().twoSum(nums1, target))