"""
Max Inserts to Obtain String Without 3 Consecutive 'a'

Write a function solution that, given a string S consisting of N characters,
return the maximum number of letters 'a' that can be inserted into S
(including at the front and end of S) so that the resulting string does not
contain three consecutive letter 'a'.
If string S already contains the substring "aaa", then your function should return -1

Example:
    1. Given S = "aabab", the function should return 3, because a string "aabaabaa" can be made.
    2. Given S = "dog", the function should return 8, because a string "aadaaoaagaa".
    3. Given S = "aa", the function should return 0
    4. Given S = "baaaa", the function should return -1, becuase there is a substring "aaa"

Write an efficient algorithm for the following assumptions:
    * N is an integer within the range [1, 200,000]
    * string S consists only of lowercase letter (a-z).
"""

def MaxInsert(S):
    pass


S = "aabab"
print(MaxInsert(S))

S = "dog"
print(MaxInsert(S))

S = "aa"
print(MaxInsert(S))

S = "baaaa"
print(MaxInsert(S))