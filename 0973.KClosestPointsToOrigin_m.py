"""
973. K Closest Points to Origin
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""
from typing import List
import math
import heapq

class Solution:
    """
    Facebook OA Problem
    Amazon OA Problem
    Google OA Problem
    Microsoft OA Problem
    """
    def kClosestNotSolved(self, points: List[List[int]], K: int) -> List[List[int]]:
        closest_points = []
        last_max_in_path = 2 ^ 32 - 1
        for point in points:
            path = math.pow(point[0], 2) + math.pow(point[1], 2)

            if len(closest_points) < K:
                heapq.heappush(closest_points, (-path, point))
                last_max_in_path = max(path, last_max_in_path)
            else:
                if last_max_in_path >= path:
                    heapq.heappop(closest_points)
                    heapq.heappush(closest_points, (-path, point))
                    last_max_in_path = max(path, last_max_in_path)

        return [point[1] for point in closest_points]

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        Time Complexity: O(N log N)
        Space Complexity: O(N)
        """
        points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
        return points[:K]


if __name__ == "__main__":
    testcases = [
        {'points': [[-95, 76], [17, 7], [-55, -58], [53, 20], [-69, -8], [-57, 87], [-2, -42], [-10, -87], [-36, -57],
                    [97, -39], [97, 49]],
         'K': 5, 'e': [[17, 7], [-2, -42], [53, 20], [-36, -57], [-69, -8]]},
        {'points': [[-2,-6],[-7,-2],[-9,6],[10,3],[-8,1],[2,8]], 'K': 5, 'e': [[-2,-6],[-7,-2],[-8,1],[2,8],[10,3]]},
        {'points': [[1,3],[-2,2],[2,-2]], 'K': 2, 'e': [[-2,2],[2,-2]]},
        {'points': [[3, 3], [5, -1], [-2, 4]], 'K': 2, 'e': [[3, 3], [-2, 4]]},
        {'points': [[1, 3], [-2, 2]], 'K': 1, 'e': [[-2, 2]]},
        {'points': [[6, 10], [-3, 3], [-2, 5], [0, 2]], 'K': 3, 'e': [[0, 2], [-3, 3], [-2, 5]]},
    ]
    for case in testcases:
        actual_result = Solution().kClosest(case['points'], case['K'])
        print("Input: {}\nExpected: {}\nAcutal: {}\nis_Passed: {}".format(case['points'],
                                                                          case['e'],
                                                                          actual_result,
                                                                          actual_result == case['e']))

