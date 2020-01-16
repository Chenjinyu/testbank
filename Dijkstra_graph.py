"""
Undirected Graph

A --5-- B --1-- D --6-- F
|       |      / |
|       2    4   3
|       |  /     |
 1 ---- C --8--- E

the number represents the step/weight. eg, from A to B, it needs 5 steps

# Dijkstra algorithm
# priority Queue, the API algorithm in two aspects:
# 1. we use zero-based indexing. this makes the relationship between the index for a node
# and the indexes for its children slightly less obvious. but is more suitable since Python
# use zero-based indexing.
# 2. Our pop method returns the smallest item, not the largest(called a "min heap" in textbooks,
# a "max heap" is more common in texts because of its suitable for in-place sorting)

# so the priority queue(heapq) heappop the smallest one first, and so on.

https://www.youtube.com/watch?v=9wV1VxlfBlI
"""


import heapq, math
from collections import defaultdict

# heapq, is priority queue, which has
# pqueue = []
# heapq.heappush(pqueue, (1, 'A'))
# heapq.heappush(pqueue, (5, 'B'))
# heapq.heappush(pqueue, (4, 'C'))
# heapq.heappush(pqueue, (8, 'D'))
# heapq.heappush(pqueue, (3, 'E'))
# heapq.heappush(pqueue, (9, 'F'))
#
# # the whole heapq order is different with the heappop.
# print(pqueue)
# print(heapq.heappop(pqueue))
# print(heapq.heappop(pqueue))
# print(heapq.heappop(pqueue))
# print(heapq.heappop(pqueue))
# print(heapq.heappop(pqueue))
# print(heapq.heappop(pqueue))


graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
}

# 求出从一个节点到另外一个节点的最短距离,比如从A到B的最短距离：应该是 A->C->B: 3, 而不是A-B:5.


def init_distance(graph, start):
    distance = {start: 0}
    for vertex in graph:
        if vertex is not start:
            distance[vertex] = math.inf
    return distance


def dijkastra(graph, start):
    pqueue = []
    heapq.heappush(pqueue, (0, start))
    seen = set()
    parent = {start: None}
    distance = defaultdict(lambda: math.inf)
    distance[start] = 0
    # distance = init_distance(graph, start)

    while pqueue:
        dist, vertex = heapq.heappop(pqueue)
        # base on finding the smallest path, each node will appear many times with differ dist.
        # so the seen should add the parent node, not in the for loop.
        # detail: https://www.youtube.com/watch?v=9wV1VxlfBlI
        seen.add(vertex)

        nodes = graph[vertex].keys()
        for w in nodes:
            if w not in seen:
                if dist + graph[vertex][w] < distance[w]:
                    distance[w] = dist + graph[vertex][w]
                    parent[w] = vertex
                    heapq.heappush(pqueue, (dist + graph[vertex][w], w))

    return parent, distance


parent, distance = dijkastra(graph, "A")
# ({'A': None, 'B': 'C', 'C': 'A', 'D': 'B', 'E': 'D', 'F': 'D'}, {'A': 0, 'B': 3, 'C': 1, 'D': 4, 'E': 7, 'F': 10})
# so from A to F, the smallest distance is 10
# the path base on the parent dict
k = 'F'
print(k)
while parent[k]:
    print(parent[k])
    k = parent[k]
