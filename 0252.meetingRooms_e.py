"""
252. Meeting Rooms
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
determine if a person could attend all meetings.

Example 1:
Input: [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: [[7,10],[2,4]]
Output: true
"""
from typing import List


class Solution:
    """
    Amazon OA Problem
    Microsoft OA Problem
    Bloomberg OA Problem
    """
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])

        intervals_len = len(intervals)
        for idx in range(intervals_len - 1):
            if intervals[idx][1] > intervals[idx + 1][0]:
                return False
        return True


if __name__ == "__main__":
    testcases = [
        {'s': [[0, 30], [5, 10], [15, 20]], 'e': False},
        {'s': [[7, 10], [2, 4]], 'e': True},
    ]
    is_pass = True
    for case in testcases:
        actual_result = Solution().canAttendMeetings(case['s'])
        print("Input: {}\nExpected: {}\nAcutal: {}\nis_Passed: {}".format(case['s'],
                                                                          case['e'],
                                                                          actual_result,
                                                                          actual_result == case['e']))
        if actual_result != case['e']:
            is_pass = False

    if not is_pass:
        print("!!!!-----FAILED------!!!!")