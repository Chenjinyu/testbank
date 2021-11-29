"""
347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        100 ms, faster than 91.58% of Python3
        Time Complexity: O(n log n)
        """
        if not nums:
            return []

        nums_counter = Counter(nums)
        nums_list = [(k, v) for k, v in nums_counter.items()]
        nums_list.sort(key=lambda x: x[1], reverse=True)
        nums_list.sort(key=lambda x: -x[1])
        print(nums_list)
        res = list(dict(sorted(nums_counter.items(), key=lambda x: x[1])[:k]).values())
        print(res)
        return [ans[0] for ans in nums_list[:k]]

    def topKFrequentImprove(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        nums_counter = Counter(nums)
        ans = []
        max_val = float('-inf')
        for k, v in nums_counter.items():
            max_val = max(max_val, v)
            if max_val == v:
                if len(ans) >= k:
                    ans = ans[1:]
                ans.append((k, v))

        return ans



if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution().topKFrequent(nums, k))