"""
Divisibility of Strings. As part of an assignment, a student is required to find whether a given string s
is divisible by string t. If it is divisible, the student needs to find the length of the smallest string x
such that if x is concatenated any number of times, we get both s and t. If this is not possible, print -1.
"""

def find_smallest_divisor(s, t):
    if len(s) % len(t) != 0:
        return -1

    tmp_str = ''
    for i in range(len(s) // len(t)):
        tmp_str += t

    if s != tmp_str:
        return -1

    sub_str = ''
    left, right = 0, 1
    while len(sub_str) < len(t):
        sub_str = t[left:right]
        times = len(t) // len(sub_str)
        if times * sub_str == t:
            return len(sub_str)
        else:
            right += 1

    return -1