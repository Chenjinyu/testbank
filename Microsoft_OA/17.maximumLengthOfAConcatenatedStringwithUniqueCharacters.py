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
        if not arr: return 0
        end_state = (1 << 27) - 1

        def get_state(w):
            state = 0
            for c in w:
                idx = ord(c) - ord('a')
                if state & 1 << idx != 0:
                    return end_state
                state = state | 1 << idx
            return state

        states = [get_state(w) for w in arr]

        memo = dict()

        def recur(i, state):
            if state & states[i] != 0:
                return 0
            elif states[i] == end_state:
                return 0
            if (i, state) in memo: return memo[i, state]

            state = state | states[i]
            if i != len(arr) - 1:
                max_value = max(recur(j, state) for j in range(i + 1, len(arr)))
            else:
                max_value = 0
            return max_value + len(arr[i])

        return max(recur(i, 0) for i in range(len(arr)))


arr = ["cha","r","act","ers"]
print(Solution().maxLength(arr))