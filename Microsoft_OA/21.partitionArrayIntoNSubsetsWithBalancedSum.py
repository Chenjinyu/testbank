"""
Partition array into N subsets with balanced sum

Give you one sorted array, please put them into n buckets, 
we need to ensure we get n sub array with approximately equal weights.
Example;
input {1, 2, 3, 4, 5} n = 3
output [[[5],[1,4],[2,3]];
"""

import heapq

"""
T(C) => O(N Log (N)) (For Heap => O(N Log(K)) + For Sorting => O(N Log(N))
"""


def subset(arr, n):
    heap = [(0, i) for i in range(n)]
    res = [[] for _ in range(n)]
    sorted(arr, reverse=True)
    for each in arr:
        val, idx = heapq.heappop(heap)
        total = val + each
        res[idx].append(each)

        heapq.heappush(heap, (total, idx))

    return res


ip = [1, 2, 3, 4, 5, 2, 2, 3, 9]
total_subsets = 3
print(subset(ip, total_subsets))