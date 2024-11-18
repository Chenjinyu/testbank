"""
239. Sliding Window Maximum
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:

Could you solve it in linear time?

"""
from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        if length == 0:
            return []

        if length < k:
            return [max(nums)]

        left, right = 0, k
        max_slide_window_list = []
        while right <= length:
            max_slide_window_list.append(max(nums[left:right]))
            right += 1
            left += 1

        return max_slide_window_list

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]: # does not work
        if len(nums) <= 1:
            return nums
        answer = []
        my_deque = deque()
        max_sliding_wind_num = 0
        for idx in range(len(nums) - k):
            len_k = 0
            if len(answer) == 0:
                while len_k <= k:
                    cur_num = nums[idx + len_k]
                    max_sliding_wind_num += cur_num
                    my_deque.append(cur_num)
                    len_k += 1
            else:
                old_val = my_deque.popleft()
                max_sliding_wind_num -= old_val
                new_val = nums[idx + k - 1]
                my_deque.append(new_val)
                max_sliding_wind_num += new_val
            answer.append(max_sliding_wind_num)
            
        return answer


if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(Solution().maxSlidingWindow(nums, k))