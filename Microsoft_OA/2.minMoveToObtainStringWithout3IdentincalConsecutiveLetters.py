"""
2. Min Moves to Obtain String Without 3 Identical Consecutive Letters

You are given a string S consisting of N letters 'a' and/or 'b'.
In one more, you can swap one letter for the other ('a' for 'b' or 'b' for 'a')

Write a function solution that, given such a string S, returns the minimum number of moves required to obtain a string
containing no instances of three identical consecutive letters.

Example1:
    Given S = 'baaaaa', the function should return 1,
    Explanation: the string without three idential consecutive letters which can be obtained in one move is "baabaa".

Example2:
    Given S = "baaabbaabbba", the function should return 2.
    Explanation: there are four valid strings obtainable in two moves:
    for example: "bbaabbaabbaa"

Example3:
    Give S = "baabab", the function should return 0

Write an efficient algorithm for the following assumptions:
    * N is an integer within the range [0..200,000]
    * string S consist only of the characters "a" and/or "b"
"""
from itertools import groupby

class Solution:
    def minMoveToObtainString(self, S: str) -> int:
        max_move = 0
        for _, g in groupby(S):
            max_move += len(list(g)) // 3
        return max_move


if __name__ == "__main__":
    S = 'baaaaabbbbaaaa'
    print(Solution().minMoveToObtainString(S))
    print([list(g) for k, g in groupby('baaaaabbbbaaaa')])
