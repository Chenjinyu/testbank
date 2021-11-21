"""
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


