"""
253. Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
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