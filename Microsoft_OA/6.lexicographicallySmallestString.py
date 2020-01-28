"""
Lexicographically Smallest String


Lexicographically smallest string formed by removing at most one character.

Example 1:
Input: "abczzzd"
Output: "abcd"
"""

def removeAtMostOneChar(S):
    max_char = float('-inf')
    for char in S:
        max_char = max(ord(char), max_char)
    return S.replace(chr(max_char), '', 1)


S = "abczd"
print(removeAtMostOneChar(S))
