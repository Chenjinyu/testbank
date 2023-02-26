"""
https://leetcode.com/problems/path-crossing/
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

 
Example 1:
Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.

Example 2:
Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
"""
class Solution:
    def isPathCrossingWrongSol(self, path: str) -> bool:
        """
        should not check the path returns to the start, should be the cross points
        """
        # start = (0, 0)
        # north = (0, 1)
        # south = (0, -1)
        # east = (1, 0)
        # west = (-1, 0)
        path_list = []
        for p in path:
            if p == 'N':
                path_list.append(((0, 1)))
            if p == 'S':
                path_list.append((0, -1))
            if p == 'E':
                path_list.append((1, 0))
            if p == 'W':
                path_list.append((-1, 0))    
        print(path_list)
        
        prefix_sum_path_list = [path_list[0]]
        print(prefix_sum_path_list)
        for idx in range(1, len(path_list)):
            prefix_sum_path_list.append((path_list[idx][0] + prefix_sum_path_list[-1][0], path_list[idx][1] +  prefix_sum_path_list[-1][1]))
        print(prefix_sum_path_list) 
        return (0, 0) in prefix_sum_path_list
    
    def isPathCrossing(self, path: str) -> bool:
        path_set = set()
        (x, y) = (0, 0)
        path_set.add((x, y))
        for i in path:
            if i == 'N': y += 1
            elif i == 'E': x += 1
            elif i == 'S': y -= 1
            elif i == 'W': x -= 1
            if (x, y) in path_set: return True
            path_set.add((x, y))
        return False
    
print(Solution().isPathCrossing('NESWW'))