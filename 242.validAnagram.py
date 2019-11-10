"""
Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

Note:
    The all() method returns:
       * True - If all elements in an iterable are true
       * False - If any element in an iterable is false
"""
from collections import Counter
import string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_counter = Counter(s)
        # t_counter = Counter(t)
        # return s_counter == t_counter
        return all([s.count(c) == t.count(c) for c in string.ascii_lowercase])

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))