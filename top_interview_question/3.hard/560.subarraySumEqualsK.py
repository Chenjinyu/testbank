"""
560. Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

Problem Solving:
resolve this problem, like get the sum of nums[i:j], would like to use prefix sums.
prefixSum[x] = sum of sub_list[0, x] = nums[0] + nums[1] + ... + nums[x]
so, prefixSum[x] = prefixSum[x-1] + sums[x]

sum of sub_list[i:j] = prefixSum[j] - prefixSum[i - 1]
prefixSum[j] = nums[0] + nums[1] + ... + nums[i - 1]    + num[i] + ... + nums[x]
prefixSum[i- 1] = nums[0] + nums[1] + ... + nums[i - 1]
eg:
sum of sub_list[2:4] = prefixSum[4] - prefixSum[1], because prefixSum[4] = prefixSum[1] + sum(sub_list[1:4])
so, there if we want to get sub_list[0:4] which equals prefixSum[4] - prefixSum[0-1].
we need the `0` at the begin of prefixSum list.

-----

after we know the basic concept, prefixSum[x] = prefixSum[x-1] + sums[x].
for this question, we want to find how many sum of sub_list equals k.

if i < j, prefixSum[j] - prefixSum[i] == k ?
using a hashMap(dict or defaultdict) to store <prefixSum_value, #_of_occurrence_of_the_prefixSum_value>
so: hash_map = defaultdict(int); hash_map[0] = 1  => {[0, 1]}.

in a loop, check how many [prefixSum_value - k] in the hash_map, and count += hash_map[prefixSum_value-k]

"""
from typing import List
from itertools import accumulate
from collections import defaultdict


class Solution:
    def subarraySumWorstExample(self, nums: List[int], k: int) -> int:
        # Time: O(n^3), Space: O(1)
        length = len(nums)
        count = 0
        for i in range(length):
            for j in range(i, length):
                sums = 0
                for index in range(j, length):
                    sums += nums[index]
                if sums == k:
                    count += 1
        return count

    def subarraySumBetter(self, nums: List[int], k: int) -> int:
        # Time: O(n^2), Space: O(1)
        length = len(nums)
        count = 0
        for i in range(length):
            prefix_sum = 0
            for j in range(i, length):
                prefix_sum += nums[j]
                if prefix_sum == k:
                    count += 1
        return count

    def subarraySumImprove(self, nums: List[int], k: int) -> int:
        length = len(nums)
        accumulate_prefix = [0] + list(accumulate(nums))
        d_dict = defaultdict(int)
        count = 0
        for i in range(length):
            print(d_dict)
            d_dict[accumulate_prefix[i]] += 1
            print(accumulate_prefix[i])
            print(accumulate_prefix[i + 1])
            count += d_dict[accumulate_prefix[i + 1] - k]
            print("count += " + str(d_dict[accumulate_prefix[i + 1] - k]))
        return count

    def subAarryPrefixSums(self, nums: List[int], k: int) -> int:
        count = prefix_sums = 0
        length = len(nums)
        hash_map = defaultdict(int)
        hash_map[0] = 1
        for i in range(length):
            prefix_sums += nums[i]  # get the accumulate sub set.
            # this is very important, this is find #_of_occurrence_of_the_prefixSum_value in the hash_map.
            count += hash_map[prefix_sums - k]
            # increase 1 for prefixSum_vale in the hash_map.
            hash_map[prefix_sums] += 1
        return count


if __name__ == "__main__":
    # nums = [-1, 2, -1]
    # k = 1
    # nums = [-1, 1, -1]
    # nums = [-1, -1, 1]
    # k = 1

    # nums = [0, 0, 0]
    # k = 1
    nums = [3, 4, 7, 2, -3, 1, 4, 2]
    k = 7
    print(Solution().subarraySumBetter(nums, k))
