"""
Given a string s, find the length of the longest substring t that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.

Solution:
https://leetcode.com/articles/longest-substring-with-at-most-two-distinct-charac/

Knowledge extension:
defaultdict vs dict:
The defaultdict tool is a container in the collections class of Python.
It's similar to the usual dictionary (dict) container,
but the only difference is that a defaultdict will have a default value if that key has not been set yet.

eg:
example 1:
d = {}
d["k"] = 6 # rm this will raise KeyError
d["k"] += 1
print(d["k"])  # 7

from collections import defaultdict
d = defaultdict(int) # defaultdict(default_factory), like: lambda, int, float, list, str
d["k"] += 1
print(d["k"])

"""
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: 'str') -> 'int':
        """
        time complexity: O(n). space complexity: O(n)
        :param s:
        :return:
        """
        n = len(s)
        if n < 3:
            return n

        # sliding window left and right pointers
        left, right = 0, 0
        # hashmap character -> its rightmost position
        # in the sliding window
        hashmap = defaultdict()

        max_len = 2

        while right < n:
            # slidewindow contains less than 3 characters
            if len(hashmap) <= 2:
                # right position(index) to hashmap val.
                hashmap[s[right]] = right
                right += 1

            # slidewindow contains 3 characters
            if len(hashmap) == 3:
                # get the leftmost index and delete the character
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1

            # always get the max length in the while loop, until finish to slide the 's' string.
            max_len = max(max_len, right - left)

        return max_len


if __name__ == "__main__":
    s = "leeeeeeeeeeeeeeeetcoooooooooooooode"
    print(Solution().lengthOfLongestSubstringTwoDistinct(s))