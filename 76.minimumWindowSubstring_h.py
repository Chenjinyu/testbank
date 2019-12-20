"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""

import sys, math
from collections import Counter, defaultdict

class Solution:
    def min_window_final_solution(self, s, t):
        """
        this is not my solution, but the logic is very good to learn
        """
        if not s or not t or len(t) > len(s): return ""
        """
        counter t, so that fixes the duplicate characters in t.
        use count, as long as the sliding_window[char] == count_t[char]. which means in the range of 
        left and right, the s[left:right] has the same count of char with t.
        """
        count_t = Counter(t)
        sliding_window = {}
        """
        marked here increase 1 if count_t[character] == sliding_window[character]
        decrease 1 if marked==required(the s[left:right] also include all chars in t.)
        """
        l, r, marked = 0, 0, 0
        required = len(count_t)
        ans = float('inf'), None, None

        while r < len(s):
            character = s[r]
            """
            sliding_window includes all chars with the how many times it presents.
            这里的思维跟我起初试图解决问题的思路不一样。
            存储所有的char，也会在每一次的while里存储所有的最小sub_str，当然这里包括字符出现在t里的任何字符之前。
            因为，这里关心的是最终最小的值。
            """
            sliding_window[character] = sliding_window.get(character, 0) + 1
            """
            如果字符出现在count_t里，并且count_t[character] == sliding_window[character]。marked += 1
            """
            if character in count_t and count_t[character] == sliding_window[character]:
                marked += 1

            """
            在第二个while里是对left位置移动的处理。
            如果marked == required，and if left_char in t and sliding_window[left_char] < count_t[left_char]: 
            而l += 1，说明l下的char不属于t，或者说有相同的char。
            只有当marked -= 1是，推出while对left的处理。回到right的处理中。
            """
            while l <= r and marked == required:
                left_char = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                sliding_window[left_char] -= 1
                if left_char in t and sliding_window[left_char] < count_t[left_char]:
                    marked -= 1
                l += 1
            r += 1

        return "" if ans[0] == float('inf') else s[ans[1]: ans[2] + 1]

    def minWindowCouldNotPassAllTestCases(self, s: str, t: str) -> str:
        """
        why this solution could not pass all testcases, because it does not think about same character will
        be in the t string.
        also I spent a lot of time to think about how to remove the duplicated character at the begining of s.
        """
        if not s or not t or len(t) > len(s):
            return ""
        skip_pos = 0
        """there use the zip with t, if it has duplicate character, it will be removed by dict()
        so, there, this find_mark does not meet the requirement of duplicate character must be included."""
        find_mark = dict(zip(iter(t), iter([-1] * len(t))))
        ans = (0, math.pow(2, 32) - 1)
        for idx, val in enumerate(s):
            if val not in t:
                skip_pos = idx + 1
            else:
                break
        l = r = skip_pos
        while r < len(s):
            if min(find_mark.values()) == -1:
                if s[r] in t:
                    find_mark[s[r]] = r
                r += 1
            if min(find_mark.values()) >= 0:
                ans = (l, r) if ans[1] - ans[0] > r - l else ans
                if len(find_mark.values()) == 1 and min(find_mark.values()) >= 0:
                    return t
                find_mark[s[min(find_mark.values())]] = -1
                l = sorted(find_mark.values())[1]

        return "" if ans[0] == 0 and ans[1] == math.pow(2, 32) - 1 else s[ans[0]:ans[1]]
        
        

if __name__ == "__main__":
    testcases = [
        {'s': "FADOBECODEBANC", 't': 'ABC', 'e': 'BANC'},
        {'s': "abc", 't': 'ab', 'e': 'ab'},
        {'s': "aaa", 't': 'aa', 'e': 'aa'},
        {'s': "a", 't': 'a', 'e': 'a'},
        {'s': "ab", 't': 'b', 'e': 'b'},
        {'s': "aaa", 't': 'bb', 'e': ''},
        {'s': "a", 't': 'b', 'e': ''},
        {'s': "abc", 't': 'bc', 'e': 'bc'},
        {'s': "aaaabc", 't': 'bc', 'e': 'bc'},
        {'s': "bdab", 't': "ab", 'e': "ab"},
        {'s': "aab", 't': "aab", 'e': "aab"},
        {'s': "bbbbbba", 't': "ab", 'e': "ba"},

    ]
    for case in testcases:
        actual_result = Solution().min_window_final_solution(case['s'], case['t'])
        print("Input: {}\nSubStr: {}\nExpected: {}\nAcutal: {}\nis_Passed: {}".format(case['s'], case['t'],case['e'], actual_result, actual_result== case['e']))
