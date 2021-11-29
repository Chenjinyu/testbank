"""
1ST Coding Question:
Given an array of words such as ["cat", "dog", "dog"]
and given an array of patterns such as ["a", "b", "b"]
return True if the words map to patterns
(such as cat maps to a, dog maps to b, and we return True since all patterns match)

Example:
["cat", "dog", "dog"]
["a", "b", "b"]
returns True

["hat", "mat", "kick"]
["a", "b", "a"]
returns False
"""

from collections import defaultdict


def array_pattern_mapping(list1, list2) -> bool:
    arr_len = len(list1)
    arr_len2 = len(list2)
    if arr_len != arr_len2: return False

    res_dict = defaultdict(set)
    for idx in range(arr_len):
        res_dict[list2[idx]].add(list1[idx])
        # check if the set length > 1, return False.
        if len(res_dict[list2[idx]]) > 1:
            return False

    return True

#
# list1 = ["hat", "mat", "kick"]
# list2 = ["a", "b", "a"]

list1 = ["cat", "dog", "dog"]
list2 = ["a", "b", "b"]
print(set(zip(list1,list2)))
# print(array_pattern_mapping(list1, list2))
print('a' in 'abc')


