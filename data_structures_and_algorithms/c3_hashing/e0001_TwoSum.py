"""
Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 3, 6, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
 
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # runtime: 1200ms
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
        # runtime: 824ms
        for idx in range(len(nums)):
            result = target - nums[idx]
            if result in nums:
                result_idx = nums.index(result)
                if result_idx != idx:
                    return [idx, result_idx]
        return [-1, -1]
                
                
    def twoSumWithTwoPointers(self, nums: List[int], target: int) -> List[int]:
        """
        Given a sorted of array of unqiue integers and a target integer. 
        """
        left, right = 0, len(nums) - 1
        while left < right:
            curr_val = nums[right] + nums[left]
            if curr_val == target:
                return True
            elif curr_val > target:
                # since it's orded array, curr_val > target, only can move the right to the left
                # otherwise, moving left to right, the curr_val keeps bigger than target.
                right -= 1
            else:
                left += 1
            
        return False
            
            
    def twoSumWithHaskMap(self, nums: List[int], target: int) -> List[int]:
        # Runtime 59ms
        dict_nums = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in dict_nums: # This Operation is O(1)
                return [dict_nums[complement], i]
            
            dict_nums[num] = i
            
        return [-1, -1]


import unittest
class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_twoSumRedo(self):
        nums = [1, 2, 3, 4, 5]
        tgt = 6
        result = self.solution.twoSumRedo(nums, tgt)
        expect = [0,4]
        self.assertEqual(result, expect)
        

if __name__ == "__main__":
    nums1 = [2,7,11,15]
    target = 9
    print(Solution().twoSumWithHaskMap(nums1, target))
    # unittest.main()
