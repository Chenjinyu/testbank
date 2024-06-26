[Good to start to know different data structure of Python](https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm)

### Sorted

func: sorted(iterable, *, key=func, reverse=False)
eg. 
* sorted(strs, key=len)
* sorted(strs, key=lambda x: x*2)
* sorted(strs, key=str.lower)
* sorted(student_objects, key=attrgetter('age'))
* sorted(student_objects, key=attrgetter('age'), reverse=True)

        
```
>>>from operator import itemgetter, attrgetter
>>>sorted(student_tuples, key=itemgetter(2))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
>>> sorted(student_objects, key=attrgetter('age'))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]


# order by grade and age.
>>> sorted(student_tuples, key=itemgetter(1,2))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
>>> sorted(student_objects, key=attrgetter('grade', 'age'))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
```

#### Ascending and Descending
Both list.sort() and sorted() accept a reverse parameter with a boolean value. This is used to flag descending sorts. For example, to get the student data in reverse age order:
```
>>> sorted(student_tuples, key=itemgetter(2), reverse=True)
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

>>> sorted(student_objects, key=attrgetter('age'), reverse=True)
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
```

### defaultdict vs dict:
The defaultdict tool is a container in the collections class of Python.
It's similar to the usual dictionary (dict) container,
but the only difference is that a defaultdict will have a default value if that key has not been set yet.

eg:
```python
d = {}
d["k"] = 6 # rm this will raise KeyError
d["k"] += 1
print(d["k"])  # 7
```

```python
from collections import defaultdict
d = defaultdict(int) # defaultdict(default_factory), like: lambda, int, float, list, str
d["k"] += 1
print(d["k"])
```

```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]
hash = {k:v for k, v in zip(keys, values)}
print(hash)
# {'a': 1, 'c': 3, 'b': 2}
```

### Slice of List
```python
test = [1,3,-1,-3,5,3,6,7]
print(test[5:len(test)]) # the slice end of before len(test), not including the len(test)
print(test[0:3]) # starts from 0, the 3 means index of 3, not including the index 3.
```


### xrange vs range
[Python 3's range is more powerful than Python 2's xrange](https://treyhunner.com/2018/02/python-3-s-range-better-than-python-2-s-xrange/)

### Tree
1. Depth-First Search (DFS) strategy. example: [easy 1](0104.maximumDepthOfBinaryTree_e.py)
2. Breadth-First Search (BFS) strategy

### heapq 
* `import heapq`. heapq is a binary heap, with O(logn) push and pop.
  - `heapq.heapify()` transform list x into a heap, in-place, in liner time. Time complexity: O(N).
  - `eapq.heappop(heap)`, pop and return the smallest item from the heap, maintaining the heap invariant. if the heap is empty, IndexError is raised.
  - `heapq.heappush(heap, item)`, push the value item onto the heap, maintaining the heap invariant.
  
### Queue vs Stack
* 队列是一种先进先出（First In First Out，FIFO）的数据结构，而栈是一种后进先出（Last In First Out，LIFO）的数据结构
