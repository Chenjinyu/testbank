"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.
explain: the first non-repeating character is l

s = "loveleetcode",
return 2. explain: the first non-repeating character is v.

Note: You may assume the string contain only lowercase letters.

memory test:  python -m memory_profiler 387.firstUniqueCharacterInaString.py
======
Filename: 387.firstUniqueCharacterInaString.py

Line #    Mem usage    Increment   Line Contents
================================================
    18   11.461 MiB   11.461 MiB       @profile
    19                                 def firstUniqChar(self, s: str) -> int:
    20   11.461 MiB    0.000 MiB           s_counter = Counter(s)
    21   11.469 MiB    0.008 MiB           print(s_counter)
    22   11.469 MiB    0.000 MiB           if 1 not in s_counter.values():
    23                                         return -1
    24
    25   11.469 MiB    0.000 MiB           matched_index = []
    26   11.469 MiB    0.000 MiB           for k, v in s_counter.items():
    27   11.469 MiB    0.000 MiB               if v == 1:
    28   11.469 MiB    0.000 MiB                   matched_index.append(s.find(k))
    29
    30   11.469 MiB    0.000 MiB           return min(matched_index)

"""

from collections import Counter

class Solution:
    """
    Amazon OA Problem
    Apple OA Problem
    Microsoft OA Problem
    """
    @profile
    def firstUniqChar(self, s: str) -> int:
        s_counter = Counter(s)
        print(s_counter)
        if 1 not in s_counter.values():
            return -1

        matched_index = []
        for k, v in s_counter.items():
            if v == 1:
                matched_index.append(s.find(k))

        return min(matched_index)


if __name__ == "__main__":
    s = "leetcode"
    print(Solution().firstUniqChar(s))
