"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

"""
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict()
        for s in strs:
            str_order = "".join(sorted(s))
            if str_order in result.keys():
                result[str_order] = result[str_order] + [s]
            else:
                result[str_order] = [s]
        return result.values()

    def groupAnagramsDictImprove(self, strs: List[str]) -> List[List[str]]:
        # create a default dict which value is list with empty value.
        result = defaultdict(list)
        for s in strs:
            str_order = "".join(sorted(s))
            result[str_order].append(s)
        return result.values()


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagramsDictImprove(strs))
