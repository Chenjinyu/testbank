"""
27. Remove Element

Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.


Problem solving：
why use nums[:] here, please take a look: top_interview_question/1.esay/26.26.removeDuplicatesFromSortedArrary.py
class Solution:
    def removeElement(self, nums, val) -> int:
        print(hex(id(nums)))
        nums[:] = [v for v in nums if v != val] (Runtime: 36 ms, faster than 90.53% of Python3 online submissions for Remove Element.)
        # or
        nums[:] = filter(lambda x: x != val, nums) (Runtime: 44 ms, faster than 31.48% of Python3 online submissions for Remove Element.)
        print(hex(id(nums)))
        return len(nums)
"""


class Solution:
    def removeElement(self, nums, val) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums[:] = [v for v in nums if v != val]
        nums[:] = filter(lambda x: x != val, nums)
        return len(nums)


if __name__ == "__main__":
    input_list = [0,1,2,2,3,0,4,2]
    val = 2
    print(Solution().removeElement(input_list, val))

