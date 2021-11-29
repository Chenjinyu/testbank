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

NOTE: input types have been changed on April 15, 2019.
Please reset to default code definition to get new method signature.
"""
from typing import List
import heapq


class Solution:
    """
    compare the end of date with the next of start datetime, insert the end datetime to heapq to compare with
    the next start datetime.
    heapq re-order the order from low to high value.
    """
    def min_meeting_rooms(self, intervals: List[List[int]]) -> int:
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals: return 0
        # Sort the meetings in increasing order of their start time.
        intervals.sort(key=lambda x: x[0])
        # The heap initialization
        free_room = []
        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_room, intervals[0][1])

        # For all the remaining meeting rooms
        for interval in intervals[1:]:
            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_room[0] <= interval[0]:
                heapq.heappop(free_room)
            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_room, interval[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_room)


interval_lst = [[0, 30], [5, 10], [15, 20]]
print(Solution().min_meeting_rooms(interval_lst))
