"""
String Without 3 Identical Consecutive Letters

Write a function solution that, given a string S of N lowercase English letters.
returns a string with no instances of three identical consecutive letters,
obtained from S by deleting the minimum possible number of letters.

Example1:
    Given S = "eedaaad", the function should return "eedaaad".
    One occurrence of letter 'a' is deleted.
Example2:
    Given S = "uuuuxaaaaaxuuu", the function return "uuxaaxuu"

Write an efficient algorithm for the following assumptions:
    * N is an integer within the range [1..200,000]
    * string S consistent only of lowercases letter[a-z]
"""

from itertools import groupby

class Solution:
    def three_identical_consecutive_letters(self, S) -> str:
        pass

if __name__ == "__main__":
    S = "uuuuxaaaaaxuuu"
    print(Solution().three_identical_consecutive_letters(S))