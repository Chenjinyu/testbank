"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

solution:
combine to int, and +1, split to int list.
"""
class Solution:
    def plusOne(self, digits):
        array_int = int("".join([str(v) for v in digits]))
        array_int += 1
        array_int_list = [int(i) for i in str(array_int)]
        return array_int_list


if __name__ == "__main__":
    nums1 = [4,9,9,9,9]
    print(Solution().plusOne(nums1))