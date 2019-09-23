"""
26. Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


Problem solving：
1. the items in set() are non-duplicated, otherwise, set(list) will remove the duplicated items.
2. read the description carefully, it says **in-place**, which means the nums address should not be changed.
3. although it asks to return the length of list, it also check the address of nums if you removed the item in nums self.
4. use nums[:] instead of nums. eg nums = sorted(list(set(nums))) is WRONG. they are two different addresses.
5. well, make sure `sorted` them, to pass all of the test case, they might not give you a sorted list input.

class Solution:
    def removeDuplicates(self, nums) -> int:
        print(hex(id(nums)))
        nums[:] = sorted(list(set(nums)))
        print(hex(id(nums)))
        return len(list(set(nums)))
"""


class Solution:
    def removeDuplicates(self, nums) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(list(set(nums)))
        return len(list(set(nums)))


if __name__ == "__main__":
    input_list = [1, 1, 2]
    print(Solution().removeDuplicates(input_list))

