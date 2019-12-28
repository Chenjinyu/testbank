"""
238. Product of Array Except Self
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product(乘积) of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division（除法） and in O(n).

Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the purpose of space complexity analysis.)
"""
from typing import List
from functools import reduce
class Solution:
    """
    Amazon OA Problem
    Facebook OA Problem
    Oracle OA Problem
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Time Limit Exceeded
        """
        output = []
        for idx in range(len(nums)):
            output.append(reduce(lambda x, y: x * y, [x for i, x in enumerate(nums) if idx != i]))

        return output

    def productExceptSelfImprove(self, nums: List[int]) -> List[int]:
        """
        time complexity: O(num_len)
        space complxity: O(num_len)
        dynamic programming.
        """
        if not nums: return []
        num_len = len(nums)
        output = [1] * num_len
        # the first loop to get the left result.
        for idx in range(1, num_len):
            output[idx] = nums[idx - 1] * output[idx - 1]

        right = 1
        # the right is the product of left result.
        for idx in range(num_len - 1, -1, -1):
            output[idx] = right * output[idx]
            right = right * nums[idx]

        return output


if __name__ == "__main__":
    testcases = [
        {'s': [1,2,3,4], 'e': [24,12,8,6]},
    ]
    is_pass = True
    for case in testcases:
        actual_result = str(Solution().productExceptSelfImprove(case['s']))
        print("Input: {}\nExpected: {}\nAcutal: {}\nis_Passed: {}".format(case['s'],
                                                                          case['e'],
                                                                          actual_result,
                                                                          actual_result == case['e']))
        if actual_result != case['e']:
            is_pass = False

    if not is_pass:
        print("!!!!-----FAILED------!!!!")