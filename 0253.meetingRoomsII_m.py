"""
253. Meeting Rooms II
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

Example 1:
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:
Input: [[7,10],[2,4]]
Output: 1
"""
from typing import List
import heapq

class Solution:
    """
    Facebook OA Problem
    Amazon OA Problem
    Microsoft OA Problem
    Google OA Problem
    Oracle OA Problem
    """
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Time Complexity: O(N log N). the sorting of the array takes O(N log N).
        and the loop with the min-heap takes O(N log N) with worse case. because the extract-min operation takes O(log N)
        and the loop takes O(N)
        Space Complexity: O (N)
        """
        if not intervals: return 0
        intervals.sort(key=lambda x: x[0])
        free_room = []
        heapq.heappush(free_room, intervals[0][1])

        for interval in intervals[1:]:
            # compare with the min sorted list by first item in free_room which is the end time.
            # 1. push 17. 2. push 5, [5,17], 3. 5 > 4, push 8, [5,8,17], 4. 5 > 4: push 5. so [5,5,8,17]
            if free_room[0] <= interval[0]:
                heapq.heappop(free_room)

            heapq.heappush(free_room, interval[1])

        return len(free_room)


if __name__ == "__main__":
    testcases = [
        {'s': [[4, 17], [4, 5], [4, 8], [4, 5]], 'e': 4},
        {'s': [[4, 9], [4, 17], [8, 10], [9, 18]], 'e': 3},
        {'s': [[0, 30], [5, 10], [15, 20]], 'e': 2},
        {'s': [[9, 10], [4, 9], [4, 17]], 'e': 2},
        {'s': [[2, 11], [6, 16], [11, 16]], 'e': 2},
        {'s': [[7, 10], [2, 4]], 'e': 1},
    ]
    is_pass = True
    for case in testcases:
        actual_result = Solution().minMeetingRooms(case['s'])
        print("Input: {}\nExpected: {}\nAcutal: {}\nis_Passed: {}".format(case['s'],
                                                                          case['e'],
                                                                          actual_result,
                                                                          actual_result == case['e']))
        if actual_result != case['e']:
            is_pass = False

    if not is_pass:
        print("!!!!-----FAILED------!!!!")