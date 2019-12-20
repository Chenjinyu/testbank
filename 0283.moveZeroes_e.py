"""
283. Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for v in nums:
            if v == 0:
                nums.remove(v)
                nums.append(0)


if __name__ == "__main__":
    nums1 = [0, 0, 1]
    (Solution().moveZeroes(nums1))
    print(nums1)