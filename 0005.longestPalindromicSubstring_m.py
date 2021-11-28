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
    """
    Amazon OA Problem
    Microsoft OA Problem
    Apple OA Problem
    Google OA Problem
    Facebook OA Problem
    Cisco OA Problem
    Uber OA Problem
    Yahoo OA Problem
    Samsung OA Problem
    """
    def longestPalindrome(self, s: str) -> str:
        """
        time complexity: O (N^3), coz sub_str[::-1]
        :param s:
        :return:
        """
        s_len = len(s)
        if not s_len:
            return ""

        palin = ''
        if s_len <= 2:
            return s if s == s[::-1] else s[0]
        else:
            for i in range(s_len):
                for j in range(i, s_len + 1):
                    # should be s_len + 1, coz s[i:j], the [i:j] is [i:j).
                    # if s = ccc, s[:3] = ccc, and slice, no need to care about the out of index.
                    sub_str = s[i:j]
                    if len(sub_str) > 1 and sub_str == sub_str[::-1] and len(sub_str) > len(palin):
                        palin = sub_str
        return palin if len(palin) else s[0]


if __name__ == "__main__":
    s = "cccddd"
    print(Solution().longestPalindrome(s))

