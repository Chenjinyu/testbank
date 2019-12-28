"""
56. Merge Intervals
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""
from typing import List

class Solution:
    """
    Facebook OA Problem
    Google OA Problem
    Amazon OA Problem
    LinkedIn OA Problem
    Oracle OA Problem
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        drop, could not pass testcases
        """
        if not intervals: return []
        list_len = len(intervals)
        if list_len == 1:
            return intervals
        right = 0
        result = [[0, 0]] * list_len

        result[0] = intervals[0]
        result_idx = 0
        intervals = intervals[1:]
        while right < list_len - 1:
            origal_left = intervals[right][0]
            result_right = result[result_idx][1]
            if intervals[right][0] <= result[result_idx][1]:
                if intervals[right][0] <= result[result_idx][0]:
                    result[result_idx] = [intervals[right][0], intervals[right][1]]
                else:
                    result[result_idx] = [result[result_idx][0], intervals[right][1]]
            else:
                result_idx += 1
                result[result_idx] = [intervals[right][0], intervals[right][1]]
            right += 1
        return result[:result_idx + 1]


    def mergeSolution(self, intervals):
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

if __name__ == "__main__":
    testcases = [
        {'s': [[1,3],[2,6],[8,10],[15,18]], 'e': [[1,6],[8,10],[15,18]]},
        {'s': [[1,4],[4,5]], 'e': [[1,5]]},
        {'s': [[1,4],[0,4]], 'e': [[0,4]]},
        {'s': [[1,4],[0,1]], 'e': [[0,4]]},
    ]
    is_pass = True
    for case in testcases:
        actual_result = (Solution().merge(case['s']))
        print("Input: {}\nExpected: {}\nAcutal: {}\nis_Passed: {}".format(case['s'],
                                                                          case['e'],
                                                                          actual_result,
                                                                          actual_result == case['e']))
        if actual_result != case['e']:
            is_pass = False

    if not is_pass:
        print("!!!!-----FAILED------!!!!")