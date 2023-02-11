### Two Pointers
Two-pointers is an extremely common technique used to solve array and string problems. It involves having two integer variables that both move along an iterable. In this article, we are focusing on arrays and strings. This means we will have two integers, usually named something like i and j, or left and right which each represent an index of the array or string.

> **_Start the pointers at the edges of the input. Move them towards each other until they meet._**

Converting this idea into instructions:
- Start one pointer at the first index 0 and the other pointer at the last index input.length - 1.
- Use a while loop until the pointers are equal to each other.
- At each iteration of the loop, move the pointers towards each other. This means either increment the pointer that started at the first index, decrement the pointer that started at the last index, or both. Deciding which pointers to move will depend on the problem we are trying to solve.

**Another approach**
This method where we start the pointers at the first and last indices and move them towards each other is only one way to implement two pointers. Algorithms are beautiful because of how abstract they are - two pointers is just an idea, and it can be implemented in many ways. Let's look at another method. The following method is applicable when the problem has two iterables in the input, for example, two arrays.
> **_Move along both inputs simultaneously until all elements have been visited._**
Converting this idea into instructions:
- Create two pointers, one for each iterable. Each pointer should start at the first index.
- Use a while loop until one of the pointers reaches the end of its iterable.
- At each iteration of the loop, move the pointers forwards. This means incrementing either one of the pointers or both of the pointers. Deciding which pointers to move will depend on the problem we are trying to solve.
- Because our while loop will stop when one of the pointers reaches the end, the other pointer will not be at the end when the loop finishes. Sometimes, we need to iterate through all elements - if this is the case, you will need to write extra code here to make sure both iterables are exhausted.

pseudocode illustrating the concept:
```java
function fn(arr1, arr2):
    i = j = 0
    while i < arr1.length AND j < arr2.length:
        Do some logic here depending on the problem
        Do some more logic here to decide on one of the following:
            1. i++
            2. j++
            3. Both i++ and j++

    // Step 4: make sure both iterables are exhausted
    while i < arr1.length:
        Do some logic here depending on the problem
        i++

    while j < arr2.length:
        Do some logic here depending on the problem
        j++
```

Similar to the first method we looked at, this method will have a linear time complexity of O(n+m), where n = arr1.length and m = arr2.length if the work inside the while loop is O(1). Let's look at some examples.


> **Example 3: Given two sorted integer arrays, return an array that combines both of them and is also sorted.**

The trivial approach would be to first combine both input arrays and then perform a sort. If we have **n = arr1.length + arr2.length**, then this gives a time complexity of 
**O(n⋅logn)** (the cost of sorting). This would be a good approach if the input arrays were not sorted, but because they are sorted, we can use the two-pointers technique to improve to O(n).

provided by LeetCdoe
```python
def combine(arr_1: List[int], arr_2: List[int]) -> List[int]:
    ans = []
    idx_1 = idx_2 = 0
    while idx_1 < len(arr_1) and j < len(arr_2):
        if arr_1[idx_1] < arr_2[j]:
            ans.append(arr_1[idx_1])
            idx_1 += 1
        else:
            ans.append(arr_2[idx_2])
            idx_2 += 1
    
    while idx_1 < len(arr_1):
        ans.append(arr_1[idx_1])
        idx_1 += 1
    
    while idx_2 < len(arr_2):
        ans.append(arr_2[idx_2])
        idx_2 += 1
    
    return ans
```

> **_NOTE_**: we also can check which array's index reach to the end in the first while loop, then, append another array[index: len-1]. but this logic here will be more complicated comparing with the exampe.  since the example does not need to care about which array's length is reached to the end. so that, it can avoid some logic issues.

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # s = ace, t = abcde, it's matched.
        # check 392. Is Subsequence.
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
```

1. [392. Is Subsequence.](../../lc_2023/e0392_isSubsequence.py)