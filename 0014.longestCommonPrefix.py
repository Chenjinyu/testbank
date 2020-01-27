"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

Note:
    func: sorted(iterable, *, key=func, reverse=False)
    eg. sorted(strs, key=len)
        sorted(strs, key=lambda x: x*2)
        sorted(strs, key=str.lower)
"""
from typing import List

class Solution:
    def longestCommon(self, strs: List[str]) -> str:
        """
        compare the sub str in each item.
        :param strs:
        :return:
        """
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]

        short_length = min(list(map(lambda x: len(x), strs)))
        short_item = list(filter(lambda y: len(y) == short_length, strs))[0]
        strs.remove(short_item)
        short_matched_str = ""
        for item in strs:
            matched_str = ""
            matched_pos = -1
            start = 0
            pos = 1
            if len(item) == pos:
                if item in short_item:
                    matched_str += item
            else:
                while pos <= short_length:
                    if start == pos:
                        pos += 1
                    sub_item = short_item[start:pos]
                    if item.find(sub_item) >= 0:
                        if matched_pos <= item.find(sub_item):
                            matched_pos = item.find(sub_item)
                            matched_str += short_item[pos-1]
                    else:
                        start += 1
                    pos += 1

            pos += 1
            if short_matched_str == "":
                short_matched_str = matched_str
            elif len(matched_str) < len(short_matched_str):
                short_matched_str = matched_str

        return short_matched_str

    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        compare prefix in each item.
        :param strs:
        :return:
        """
        # strs.sort(key=len)
        strs = sorted(strs, key=len)
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]

        prefix = ''
        for index, char in enumerate(strs[0]):
            for compare_word in (strs[1:]):
                is_match = True
                if char != compare_word[index]:
                    is_match = False
                    break
            if is_match:
                prefix += char
            else:
                break
        return prefix


if __name__ == "__main__":
    strs = \
    [
        ["ought", "thought", "think", "fourth", "the"], # t
        ["dog", "racecar", "car"], # ""
        ["flower", "flow", "flight"], # fl
        ["c", "c"], # c
        ["a", "b"], # ""
        ["aa", "aa"], # aa
        ["a", "a", "b"] # ""
    ]

    for s in strs:
        print(Solution().longestCommonPrefix(s))