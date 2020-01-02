"""
340. Longest Substring with At Most K Distinct Characters
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.

"""

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        length = len(s)
        if length < k:
            return length

        left, right = 0, 0
        longest_len = 0
        pos_hashmap = defaultdict()

        while right < length:
            pos_hashmap[s[right]] = right
            right += 1

            if len(pos_hashmap) == k + 1:
                leftmost_pos = min(pos_hashmap.values())
                del pos_hashmap[s[leftmost_pos]]
                left = leftmost_pos + 1

            longest_len = max(longest_len, right - left)

        return longest_len


if __name__ == "__main__":
    s = "leeeeeeeeeeeeeeeetcoooooooooooooode"
    print(Solution().lengthOfLongestSubstringKDistinct(s, 2))