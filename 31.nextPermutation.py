"""
31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

Problem solving：
Generally spearking, let larger number moves/keeps back, and smaller number moves to front.
the second loop is very important, the range(N-1, i - 1, -1).
think about, besides the frist item, the samllest value will move to front.
if the samllest value > the first item, the first item will be replaced by the samllest one.
otherwise, you gonna get the smaller value.
"""


class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for index in range(length - 1, 0, -1):
            if nums[index] > nums[index - 1]:
                for new_index in range(length - 1, index - 1, -1):
                    if nums[new_index] > nums[index - 1]:
                        nums[new_index], nums[index - 1] = nums[index - 1], nums[new_index]
                        nums[index:] = sorted(nums[index:])
                        return  # get the value, break from the loop.
        nums.sort()


if __name__ == "__main__":
    nums = [1,3,2]
    Solution().nextPermutation(nums)
    print(nums)
