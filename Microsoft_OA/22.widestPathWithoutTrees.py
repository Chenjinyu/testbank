"""
https://leetcode.com/discuss/interview-question/447448/

"""
from typing import List
import math


def widestPath(paths: List):
    paths.sort()
    widest_path = -math.inf
    for idx in range(len(paths) - 1):
        widest_path = max(widest_path, paths[idx + 1] - paths[idx])

    return widest_path