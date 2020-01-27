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
    testcases = [
        # {'s': "eceba", 'k': 2, 'e': '3'},
        # {'s': "aa", 'k': 1, 'e': '2'},
        {'s': "leeeeeeeeeeeeeeeetcoooooooooooooode", 'k': 2, 'e': '17'},
    ]
    for case in testcases:
        actual_result = str(Solution().lengthOfLongestSubstringKDistinct(case['s'], case['k']))
        print("Input: {}\nExpected: {}\nAcutal: {}\nis_Passed: {}".format(case['s'],
                                                                          case['e'],
                                                                          actual_result,
                                                                          actual_result == case['e']))
