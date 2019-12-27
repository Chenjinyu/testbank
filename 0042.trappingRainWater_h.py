"""
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

graph: https://leetcode.com/problems/trapping-rain-water/
The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]

                      *
              *       * *   *
          *   * *   * * * * * *
          l                   r

Output: 6
"""
from typing import List

class Solution:
    def trapDrop(self, height: List[int]) -> int:
        """
        There is no doubt for using sliding window.
        for this solution, did not think about the different problems.
        like, increase at the begining, or decrease
        """
        is_decrease, is_increase = False, False
        stop_mark = False
        left, right = 0, 0
        ans = 0
        if height[0] == 0:
            height = height[1:]

        def trap_helper(sub_height):
            sub_height, higher_side = higher_checker(sub_height)
            if higher_side == "L":
                # mins number from right to left
                # sub_height[::-1]
                sub_height[::-1]
                return count_helper(sub_height)
            elif higher_side == "R":
                # mins number from left to right
                return count_helper(sub_height)

        def count_helper(sub_height):
            count = 0
            for idx in range(1, len(sub_height)):
                count += abs(sub_height[0] - sub_height[idx])
            return count

        def higher_checker(sub_height):
            # check where side is bigger
            if sub_height[0] > sub_height[len(sub_height) - 1]:
                sub_height = sub_height[1:]
            elif sub_height[0] < sub_height[len(sub_height) - 1]:
                sub_height = sub_height[0:len(sub_height) - 1]

            if sub_height[0] > sub_height[len(sub_height) - 1]:
                higher_side = "L"
            else:
                higher_side = "R"

            return sub_height, higher_side

        while right < len(height) - 1:
            left_bar = height[right]
            right_bar = height[right + 1]
            if is_increase and not is_decrease:
                if left_bar < right_bar:
                    right += 1
                    left = right
                else:
                    is_decrease = True
                    right += 1
            elif is_decrease and not is_increase:
                if left_bar < right_bar:
                    is_increase = True
                right += 1
            elif is_increase and is_decrease:
                if left_bar < right_bar:
                    right += 1
                else:
                    stop_mark = True

                if stop_mark:
                    ans += trap_helper(height[left:right + 1])
                    is_increase = False
                    stop_mark = False
                    left = right
            else:
                if left_bar < right_bar:
                    if is_decrease:
                        is_increase = True
                    right += 1
                else:
                    if not is_decrease:
                        is_decrease = True
                        left = right
                    right += 1

        return ans


    """
    Amazon OA Problem
    Microsoft OA Problem
    Facebook QA Problem
    Google QA Problem
    Apple QA Problem
    Uber QA Problem
    Oracle QA Problem
    """
    def trapSolutionOne(self, height: List[int]) -> int:
        """
        bascially, if height of right > left, take left max
        and count the divide of left_max - height[currect_left]and vice visa
        """
        ans = 0
        left_max, right_max = 0, 0

        left, right = 0, len(height) - 1

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                ans += right_max - height[right]

                right -= 1
        return ans


if __name__ == "__main__":
    testcases = [
        {'h': [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 'e': '6'},
        {'h': [0, 1, 2, 3, 6, 4, 2, 1, 4, 5, 3], 'e': '9'},
    ]
    is_pass = True
    for case in testcases:
        actual_result = str(Solution().trapSolutionOne(case['h']))
        print("Input: {}\nExpected: {}\nAcutal: {}\nis_Passed: {}".format(case['h'],
                                                                          case['e'],
                                                                          actual_result,
                                                                          actual_result == case['e']))
        if actual_result != case['e']:
            is_pass = False

    if not is_pass:
        print("!!!!-----FAILED------!!!!")
