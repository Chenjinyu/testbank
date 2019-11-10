"""
974. Subarray Sums Divisible by K

Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.


Example 1:

Input: A = [4, 5, 0, -2, -3, 1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]


Note:

1. 1 <= A.length <= 30000
2. -10000 <= A[i] <= 10000
3. 2 <= K <= 10000


Problem Solving:
Let's say there is a sub_list[i, j] whose sum is divided by K
sum of sub_list[i:j] = prefixSum[j] - prefixSum[i - 1]. (index i included in the sub_list)
because:
    prefixSum[j] = nums[0] + nums[1] + ... + nums[i - 1]    + num[i] + ... + nums[j]
    prefixSum[i- 1] = nums[0] + nums[1] + ... + nums[i - 1]

sum for any sub_list can be written as quotient * k + remainder.
Thus,
    prefixSum[x] = (quotient1 * k + remainder)
    sum of sub_list[i, j] = (quotient1 * k + remainder1) - (quotient2 * k + remainder2)
    --> sum of sub_list[i, j] =  (quotient1 - quotient2) * k + (remainder1 - remainder2)
so, if remainder1 equals remainder2, we can say the sub_list[i, j] can be divided by K.

"""

from typing import List
from itertools import accumulate
from collections import Counter

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        # Brute Force. Time: O(n^2), Space: O(1)
        count, length = 0, len(A)
        for i in range(length):
            sum = 0
            for j in range(i, length):
                sum += A[j]
                if sum % K == 0:
                    count += 1

        return count

    def subarrayDivByKSimpleThought(self, A: List[int], K: int) -> int:
        """
        1. get the prefix sum.
        2. get the remainder for each prefix_sum divided by K.
        3. find how many remainders are the same value.
        4. if two of prefix sum which the remainders are same value
        we could know the value which between the two prefix sum can be divided by K.
        so, as long as two of same remainders is 1 count.
        the formula: count_of_remainders * (count_of_remainders - 1) / 2.
        5. return count_of_remainders * (count_of_remainders - 1) / 2

        """
        prefix_sum = [0] + list(accumulate(A))
        remainders_list = []
        length = len(prefix_sum)
        for i in range(length):
            remainders_list.append(prefix_sum[i] % k)
        counter_remainders = Counter(remainders_list)
        return int(sum(c * (c - 1) / 2 for c in counter_remainders.values()))

    def subarrayDivByKImproive(self, A: List[int], K: int) -> int:
        prefix_sum_remainder = [0]
        for val in A:
            prefix_sum_remainder.append((prefix_sum_remainder[-1] + val) % K)
        print(prefix_sum_remainder)

        counter = Counter(prefix_sum_remainder)
        print(counter.items())
        return sum(v * (v - 1) / 2 for v in counter.values())

    def subarrayDivByKSolution(self, A: List[int], K: int) -> int:
        P = [0]
        for x in A:
            P.append((P[-1] + x) % K)
        print(P)

        count = Counter(P)
        print(count.items())
        return sum(v * (v - 1) / 2 for v in count.values())


if __name__ == "__main__":

    nums = [4,5,0,-2,-3,1]
    k = 5
    print(Solution().subarrayDivByKSimpleThought(nums, k))
