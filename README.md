# Test Bank

Must to understand:
#### Prefix Sums
1. [SubArrary Sum Equals K](./top_interview_question/3.hard/560.subarraySumEqualsK.py) 
2. [SubArray Sum Divisible By K](./top_interview_question/2.medium/974.subarraySumsDivisibleByK.py)

#### Greedy
**Intuition**
The problem to find maximum(or minimum) element (or sum) with a single array as the input is a good candidate to 
be solved by the greedy approach in linear time.
```
Pick the locally optimal move at each step, and that will lead to the globally optimal solution.
```

the algorithm is general and straightforward: **iterate over the array and update each step and standard set 
for such problems**:
* Current element
* Current local maximum sum (at this given point)
* Global maximum sum seen so far.

![greedy](./img/greedy.png)

1. [Maximum Subarray](./top_interview_question/1.easy/1.Array/53.maximumSubarray.py)