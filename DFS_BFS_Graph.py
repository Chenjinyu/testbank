"""
Difference between BFS and DFS

Breadth First Search
BFS stands for Breadth First Search is a vertex based technique for finding a shortest path in graph.
It uses a Queue data structure which follows first in first out. In BFS,
one vertex is selected at a time when it is visited and marked then its adjacent are visited and stored in the queue.
It is slower than DFS.
Ex-


        A
       / \
      B   C
     /   / \
    D   E   F

Output: A, B, C, D, E, F

Depth First Search
DFS stands for Depth First Search is a edge based technique.
It uses the Stack data structure, performs two stages,
first visited vertices are pushed into stack and second if there is no vertices then visited vertices are popped.
Ex-
        A
       / \
      B   C
     /   / \
    D   E   F

Output is:  A, B, D, C, E, F

BFS
1. BFS(Breadth First Search) uses Queue data structure for finding the shortest path.
2. BFS can be used to find single source shortest path in an unweighted graph,
because in BFS, we reach a vertex with minimum number of edges from a source vertex.
3. BFS is more suitable for searching vertices which are closer to the given source.
4. BFS considers all neighbors first and therefore not suitable for decision making trees used in games or puzzles.
5. The Time complexity of BFS is O(V + E) when Adjacency List is used and O(V^2) when Adjacency Matrix is used,
where V stands for vertices and E stands for edges.
6. Here, siblings are visited before the children

DFS
1. DFS(Depth First Search) uses Stack data structure.
2. In DFS, we might traverse through more edges to reach a destination vertex from a source.
3. DFS is more suitable when there are solutions away from source.
4. DFS is more suitable for game or puzzle problems. We make a decision, then explore all paths through this decision.
And if this decision leads to win situation, we stop.
5. The Time complexity of DFS is also O(V + E) when Adjacency List is used and O(V^2) when Adjacency Matrix is used,
where V stands for vertices and E stands for edges.
6. Here, children are visited before the siblings


What are BFS and DFS for Binary Tree?

A Tree is typically traversed in two ways:
Breadth First Traversal (Or Level Order Traversal)
Depth First Traversals:
 - Inorder Traversal (Left-Root-Right)
 - Preorder Traversal (Root-Left-Right)
 - Postorder Traversal (Left-Right-Root)

https://www.geeksforgeeks.org/bfs-vs-dfs-binary-tree/

Undirected Graph

A -- B -- D -- F
|    |  / |
  -- C -- E

graph = {

        }

"""
from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "C"],
    "C": ["B", "C", "D", "F"],
    "D": ["B", "C", "E", "F"],
    "E": ["D", "C"],
    "F": ["D"]
}


def BFS(graph, start):
    # queue = deque(start)
    queue = [start]
    seen = set()
    seen.add(start)
    # if want to know the shortest path between two graph nodes,
    # use the parent to store the current node's prevous node.
    parent = {start: None}
    while queue:
        # list.pop(0) out of the first item
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                parent[w] = vertex
                seen.add(w)
    return parent


parent = BFS(graph, 'A')

for v in parent:
    if v is not None:
        print(v, parent[v])


def DFS(graph, start):
    stack = [start]
    seen = set()
    seen.add(start)
    while stack:
        # list.pop() out of last item
        vertex = stack.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print(vertex)


DFS(graph, 'A')


