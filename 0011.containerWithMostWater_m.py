"""
11. Container With Most Water
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

graph: https://leetcode.com/problems/container-with-most-water/

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49

"""

from typing import List


class Solution:
    """
    Amazon OA Problem
    Apple OA Problem
    Google OA Problem
    Facebook OA Problem
    """
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = float('-inf')
        while left < right:
            most_water = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, most_water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water


if __name__ == "__main__":
    """
    before doing, think about all the extreme case, eg. --- or ++++ ++--, 00--112, etc.
    so that the solution will be more clear.
    """
    testcases = [
        {'s': " 0-1 ", 'e': '0'},
        {'s': "  0000001 ", 'e': '1'},
        {'s': "  ---  ", 'e': '0'},
        {'s': "  +++  ", 'e': '0'},
        {'s': "  +-2  ", 'e': '0'},
        {'s': "-5-", 'e': '-5'},
        {'s': "-3.134", 'e': '-3'},
        {'s': "  43", 'e': '43'},
        {'s': "words and 987", 'e': '0'},
        {'s': "4193 with words", 'e': '4193'},
        {'s': "-91283472332", 'e': '-2147483648'},
        {'s': "+1", 'e': '1'},
        {'s': "010", 'e': '10'},
    ]
    is_pass = True
    for case in testcases:
        actual_result = str(Solution().myAtoi(case['s']))
        print("Input: {}\nExpected: {}\nAcutal: {}\nis_Passed: {}".format(case['s'],
                                                                          case['e'],
                                                                          actual_result,
                                                                          actual_result == case['e']))
        if actual_result != case['e']:
            is_pass = False

    if not is_pass:
        print("!!!!-----FAILED------!!!!")