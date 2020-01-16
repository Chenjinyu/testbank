"""
0133. Clone Graph
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. 
Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

 

Example:
〇1 ---- 〇2 
|        |
〇4 ---- 〇3

Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},
{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.
 

Note:

The number of nodes will be between 1 and 100.
The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
You must return the copy of the given node as a reference to the cloned graph.
explaination: https://www.youtube.com/watch?v=_Zt6gwWRnHM
"""
import collections

# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        # neighbors is a List[Node]
        self.neighbors = neighbors

class Solution:
    """
    Amazon OA Problem
    Facebook OA Problem
    Google OA Problem
    """
    def cloneGraph(self, node: 'Node') -> 'Node':
        # hashmap restores the visit node
        hmap = {}
        q = collections.deque()
        # append the node, eg the node value is 1, so we can see from the node 1.
        # the orginal node 1 in the queue.
        q.append(node)
        # set hashmap's neighbors is [] identify the node have not been visited yet.
        hmap[node] = Node(node.val,[])

        while q:
            # node 1 pop up to current.
            current = q.popleft()
            # find if the node 1 has neighbors, obviously, it has node 2 and node 4.
            for neighbor in current.neighbors:
                # if neighbor node have not been visited, clone(create the node with neighbor's attrs)
                if neighbor not in hmap:
                    # new node has been created and push to hashmap, but it's neighbor is [].
                    newnode = Node(neighbor.val,[])
                    hmap[neighbor] = newnode
                    # queue append the original neighbor node.
                    q.append(neighbor)
                # add neighbors to current node.
                hmap[current].neighbors.append(hmap[neighbor])

        return hmap[node]

if __name__ == "__main__":
    node = {"$id": "1", "neighbors": [{"$id": "2", "neighbors": [{"$ref": "1"}, {"$id": "3",
                                                                                 "neighbors": [{"$ref": "2"},
                                                                                               {"$id": "4",
                                                                                                "neighbors": [
                                                                                                    {"$ref": "3"},
                                                                                                    {"$ref": "1"}],
                                                                                                "val": 4}], "val": 3}],
                                       "val": 2}, {"$ref": "4"}], "val": 1}
    print(Solution().cloneGraph(node))