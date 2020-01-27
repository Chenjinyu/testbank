"""
Longest Semi-Alternating Substring

You are given a string S of length N containing only characters 'a' and 'b'.
A substring (contiguous fragement) of S is called a semi-alternating substring if it does not contain three identical
consecutive characters. in other words, if does not contain either 'aaa' or 'bbb' substrings.
Note that whole S is its own substring.

Write a function:
    class Solution {public int solution(String s);}
which, given a string S, returns the length of the longest semi-alternating substring of S.


Example1:
    Given S = "baaabbabbb", your function should return 7. which is the length of 'aabbabb'
"""

from itertools import groupby


def longestAlternating(S):
    temp, ans = 0, 0
    for c, g in groupby(S):
        L = len(list(g))
        ans = max(ans, temp + min(L, 2))
        temp = temp + L if L < 3 else 2
    return ans


S = 'baaabbabbb'
print(longestAlternating(S))

S = 'babba'
print(longestAlternating(S))

S = 'abaaaa'
print(longestAlternating(S))