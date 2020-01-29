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
from itertools import groupby

def MaxInsert2(S):
    max_insert = 0
    for c, g in groupby(S):
        group_len = len(list(g))
        if c == 'a':
            if group_len >= 3:
                return -1
            else:
                count_a = S.count('a')
                rest_count = len(S) - count_a
                return (rest_count + 1) * 2 - count_a
        else:
            max_insert += 2
    if S[-1] != 'a':
        max_insert += 2

    return max_insert


def MaxInsert(S):
    count_a = S.count('a')
    if count_a >= 3:
        if S.find('aaa') == 1:
            return -1
    rest_count = len(S) - count_a
    return (rest_count + 1) * 2 - count_a


S = "aabab"
print(MaxInsert(S))

S = "dog"
print(MaxInsert(S))

S = "aa"
print(MaxInsert(S))

S = "baaaa"
print(MaxInsert(S))

# print("aabab".find('aaa'))
