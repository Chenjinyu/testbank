import math
import heapq


def minSum(num, k):
    heap = [-n for n in num]  # negate values for max-heap
    heapq.heapify(heap)  # Transform list into a heap, in-place, in O(len(x)) time

    for i in range(k):
        # Find max value
        max_value = heapq.heappop(heap)
        # Change max value to rounded half
        # use floor since we've negated the values
        heapq.heappush(heap, math.floor(max_value/2))

    # Calculate minimum sum
    return -sum(heap)  # reverse polarity again


data = [(1, 'J'), (4, 'N'), (3, 'H'), (2, 'O')]
# sort the data by first item
print(sorted(data, key=lambda x:x[0]))
data.sort(key=lambda x:x[0])  # in-place
print(data)
