"""
5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        max_pali_str = ''
        compare_str = ''
        pali_opps_pos = 0
        for x in s:
            if x in compare_str:
                if x in [compare_str[-1 + pali_opps_pos], compare_str[-2 + pali_opps_pos]]:
                    compare_str += x
                    pali_opps_pos -= 1
                else:
                    compare_str = compare_str[len(compare_str) + pali_opps_pos - 1:]
                    max_pali_str = max_pali_str if len(max_pali_str) > len(compare_str) else compare_str
                    compare_str += x
                    pali_opps_pos = 0
            else:
                if pali_opps_pos == 0:
                    max_pali_str += x
                else:
                    compare_str = compare_str[len(compare_str) + pali_opps_pos - 1:]
                    max_pali_str = max_pali_str if len(max_pali_str) > len(compare_str) else compare_str
                    compare_str += x
                    pali_opps_pos = 0

        return max_pali_str


if __name__ == "__main__":
    s = "abbbcef"
    print(Solution().longestPalindrome(s))