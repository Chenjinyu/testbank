"""
First Bad Version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:

    def firstBadVersion(self, n):  # [Time Limit Exceeded]
        """
        :type n: int
        :rtype: int
        """
        for i in range(1, n):
            if isBadVersion(i) is True:
                return i
                break
        return n

    def firstBadVersionImprove(self, n):  # (Binary Search)
        """
        mid = left + int((right - left) / 2)
        because: If you are setting mid = (left + right) / 2, you have to be very careful
        unless you are using a language that does not overflow such as Python.
        Left + Right could overflow. one way to fix this is to use left + (right - left) / 2 instead.
        for detail: https://en.wikipedia.org/wiki/Binary_search_algorithm#Implementation_issues
        Binary Search is a search algorithm that finds the position of a TARGET value within a sorted array.
        In our case, the left position is the firstBadVersion position. So return left rather than right. Coz, right is the second bad version 
        :param n:
        :return:
        """
        left = 1
        right = n
        while left < right:
            mid = left + int((right - left) / 2)
            if isBadVersion(mid) is True:
                right = mid
            else:
                left = mid + 1
        return left


def isBadVersion(n):
    return False
