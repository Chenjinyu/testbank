"""
1192. Critical Connections in a Network
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network
where connections[i] = [a, b] represents a connection between servers a and b.
Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.



Example 1:
               ___
            |-(_2_)
 ___ - - - -    |
(_1_)           |
  |   -         |
  |     -       ___
  |       - - -(_0_)
  |
 ___
(_3_)

Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

Constraints:
1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.

"""
from typing import List
from collections import defaultdict

class Solution:
    """
    Amazon OA Problem
    """
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        graph = defaultdict(set)
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)

        jump = [-1] * n
        res = []

        """
        starting from the current graph node, explore all the nodes which connect to current node
        except its parent, and return the minimum number of jump steps.
        """
        def dfs(cur: int, parent: int, level: int, jump: list, res: list, graph) -> int:
            jump[cur] = level + 1

            for child in graph[cur]:
                if child == parent:
                    continue
                elif jump[cur] == -1:
                    # not be visited
                    cur_jump = dfs(child, cur, level + 1, res, graph)
                    jump[cur] = min(jump[cur], cur_jump)
                else:
                    jump[cur] = min(jump[cur], jump[child])

            if jump[cur] == level + 1 and cur != 0:
                res.append([parent, cur])

            return jump[cur]

        dfs(0, -1, 0, jump, res, graph)

        return res


if __name__ == "__main__":
    n = 4
    connections = [[0,1],[1,2],[2,0],[1,3]]
    print(Solution().criticalConnections(n, connections))