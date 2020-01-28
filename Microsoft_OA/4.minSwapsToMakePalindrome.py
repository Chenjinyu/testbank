"""
Given a string, what is the minimum number of adjacent swaps required to convert a string into a palindrome.
If not possible, return -1.

Practice online: https://www.codechef.com/problems/ENCD12

Example 1:
Input: "mamad"
Output: 3

Example 2:
Input: "asflkj"
Output: -1

Example 3:
Input: "aabb"
Output: 2

Example 4:
Input: "ntiin"
Output: 1
Explanation: swap 't' with 'i' => "nitin"
"""
from collections import Counter

def minSwapToPalin(S):
    min_swap = 0
    str_counter = Counter(S)
    odd_item = [(k, v) for k, v in str_counter.items() if v % 2]
    if len(odd_item) > 1:
        return -1
    elif len(odd_item) == 1:
        # it's odd.
        pass
    else:
        # it's even
        pass




S = "mamaddd"
minSwapToPalin(S)