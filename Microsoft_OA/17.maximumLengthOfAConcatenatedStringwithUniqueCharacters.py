"""
1239. Maximum Length of a Concatenated String with Unique Characters
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.

Example 2:
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".

Example 3:
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26


Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.

"""
from typing import List, Set


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        return self.maxLengthDP(arr, set())

    def maxLengthDP(self, arr: List[str], seen: Set):
        if not arr:
            return 0
        elif len(set(arr[0])) == len(arr[0]) and seen.isdisjoint(arr[0]):
            return max(self.maxLengthDP(arr[1:], seen.union(arr[0])) + len(arr[0]), self.maxLengthDP(arr[1:], seen))
        else:
            return self.maxLengthDP(arr[1:], seen)


    def maxLength2(self, arr: List[str]) -> int:
        """
        bit wise: eg: abc --> 0b000111
                      efg --> 0b111000
                    abc & efg = 00000000, abc | efg = 00111111
                    so, abc & efg = 0, means there is not duplicate char.
        """
        if not arr: return 0

        def get_state(w):
            bit_state = 0
            for c in w:
                idx = ord(c) - ord('a')
                # if bit_state & 1 << idx != 0:
                #     return end_state
                bit_state |= 1 << idx
            return bit_state

        states = [get_state(w) for w in arr]

        def recur(i, state):
            if state & states[i] != 0:
                return 0

            state = state | states[i]
            if i != len(arr) - 1:
                max_value = max(recur(j, state) for j in range(i + 1, len(arr)))
            else:
                max_value = 0

            return max_value + len(arr[i])

        return max(recur(i, 0) for i in range(len(arr)))


def get_state(w):
    bit_state = 0
    for c in w:
        idx = ord(c) - ord('a')
        if bit_state & 1 << idx != 0:
            return "-1"
        bit_state |= 1 << idx
    return bit_state

arr = ["cha","r","act","ers"]
arr = ["un","iq","ue"]
# arr = ["abcdefghijklmnopqrstuvwxyz"]
print(Solution().maxLength2(arr))
# print(1 << 2)
# print(get_state("cha"))