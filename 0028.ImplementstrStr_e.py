"""
28. Implement strStr()

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


Problem solving：
well, very simple.  make sure don't use the `index`, should instead by `find`. because, `index` will raise exception if there no substr.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == "__main__":
    haystack = "aaaaa"
    needle = "bba"
    print(Solution().strStr(haystack, needle))

