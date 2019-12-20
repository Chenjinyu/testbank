"""
350. Intersection of Two Arrary II
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

"""
from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        nums1_counter = Counter(nums1)
        nums2_counter = Counter(nums2)
        result_list = []
        intersection_set = set(nums1).intersection(nums2)
        for v in intersection_set:
            val1 = nums1_counter.get(v)
            val2 = nums2_counter.get(v)
            if val1 == val2:
                result_list.extend([v] * val1)
            else:
                result_list.extend([v] * min(val1, val2))

        return result_list


if __name__ == "__main__":
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(Solution().intersect(nums1, nums2))