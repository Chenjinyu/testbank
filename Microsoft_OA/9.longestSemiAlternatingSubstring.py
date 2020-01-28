"""
Longest Semi-Alternating Substring

You are given a string S of length N containing only characters 'a' and 'b'.
A substring (contiguous fragment) of S is called a semi-alternating substring if it does not contain three identical
consecutive characters. in other words, if does not contain either 'aaa' or 'bbb' substrings.
Note that whole S is its own substring.

Write a function:
    class Solution {public int solution(String s);}
which, given a string S, returns the length of the longest semi-alternating substring of S.


Examples:
    Given S = "baaabbabbb", your function should return 7. which is the length of 'aabbabb'
    Given S = "babaa", your function should return 5. since whole S is semi-alternating.
    Given S = "abaaaa", your function sohuld return 4, because the first four letters of S create a semi-alternating substring.

Write an efficient algorithm for the following assumptions:
    * N is an integer within the range [1..200,000]
    * string S consist only of the characters "a" and/or "b"
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