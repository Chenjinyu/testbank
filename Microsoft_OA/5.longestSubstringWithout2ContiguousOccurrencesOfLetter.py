"""
Longest Substring Without 2 Contiguous Occurrences of Letter

Given a string s containing only a and b, find longest substring of s such that S does not contain
more than two contiguous occurrences of a and b.

Example 1:
Input: "aabbaaaaabb"
Output: "aabbaa"

Example 2:
Input: "aabbaabbaabbaa"
Output: "aabbaabbaabbaa"
"""

from itertools import groupby


def longestSubstringWithoutTwoContiguousOccurrencesOfLetter(S):
    if len(S) < 3:
        return S
    max_substring, substring = "", ""
    occur_count = 0
    for idx in range(len(S)):
        if not substring:
            substring += S[idx]
        else:
            if substring[-1] == S[idx]:
                if occur_count < 2:
                    substring += S[idx]
                    occur_count += 1
                else:
                    occur_count = 0
                    max_substring = substring if len(substring) > len(max_substring) else max_substring
                    substring = ""
            else:
                substring += S[idx]
                occur_count = 1
        max_substring = substring if len(substring) > len(max_substring) else max_substring

    return max_substring



S = 'aabbaaaaabbaabbaabbaabb'
print(longestSubstringWithoutTwoContiguousOccurrencesOfLetter(S))

S = 'aabbaaaaabb'
print(longestSubstringWithoutTwoContiguousOccurrencesOfLetter(S))

S = 'aabbaabbaabbaa'
print(longestSubstringWithoutTwoContiguousOccurrencesOfLetter(S))

