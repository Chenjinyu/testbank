"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        greedy algorithms.
        always compare the last one interval[1] in the output with the next interval

        """
        new_start, new_end = newInterval
        idx, length = 0, len(intervals)
        output = []

        while idx < length and intervals[idx][0] < new_start:
            output.append(intervals[idx])
            idx += 1

        # greedy algorithm starts
        if not output or output[-1][1] < new_start:
            # append newInterval and compare the output[-1][1] with next interval in the next while loop
            output.append(newInterval)
        else:
            output[-1][1] = max(output[-1][1], new_end)

        while idx < length:
            start, end = intervals[idx]

            if output[-1][1] < start:
                output.append(intervals[idx])
            else:
                output[-1][1] = max(output[-1][1], end)

            idx += 1

        return output


if __name__ == "__main__":
    # intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    # newInterval = [4, 8]
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    print(Solution().insert(intervals, newInterval))
    # print([[1, 2], [3, 10], [12, 16]])
    print([[1, 5],[6, 9]])
