## Counting

Counting is the most common hash map pattern, and since hash maps are the most common interview concept, counting is arguably the most common interview pattern. By "counting", we are referring to tracking the frequency of things. This means our hash map will be mapping keys to integers. Anytime you need to count anything, think about using a hash map to do it.

Recall that when we were looking at sliding windows, some problems had their constraint as limiting the amount of a certain element in the window. For example, longest substring with at most k 0s. In those problems, we could simply use an integer variable count because we are only focused on one element (we only cared about 0). A hash map opens the door to solving problems where the constraint involves multiple elements. Let's start by looking at a sliding window example that leverages a hash map

```html
Example 1: You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.

For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".
```

This problem deals with substrings and has a constraint on the substrings (at most k distinct characters). These characteristics let us know that we should consider sliding window. Remember, the idea of a sliding window is to add elements by sliding to the right until the window violates the constraint. Once it does, we shrink the window from the left until it no longer violates the constraint. In this problem, we are concerned with the number of distinct characters in the window. The brute force way to check for this constraint would be to check the entire window every time, which could take O(n) time. Using a hash map, we can check the constraint in O(1).

Let's use a hash map counts to keep count of the characters in the window. This means we will map letters to their frequency. The length (number of keys) in counts at any time is the number of distinct characters. When we remove from the left, we can decrement the frequency of the elements being removed. When the frequency becomes 0, we know this character is no longer part of the window, and we can delete the key.

>In Python, the collections module provides very useful data structures. We will be using a defaultdict in the Python code. Functionality-wise, a defaultdict is the same as a hash map, it's just more pleasant to work with.

```python
from collections import defaultdict

def find_longest_substring(s: str, k: int) -> int:
    counters = defaultdict(int)
    left = ans = 0

    for right in range(len(s)):
        counts[s[right]] += 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
        ans = max(ans, right - left + 1)

    return ans

```

As you can see, using a hash map to store the frequency of any key we want allows us to solve sliding window problems that put constraints on multiple elements. We know from earlier that the time complexity of sliding window problems are O(n) if the work done inside each for loop iteration is amortized constant, which is the case here due to a hash map having O(1) operations. The hash map occupies O(k) space, as the algorithm will delete elements from the hash map once it grows beyond k.

```html
Example 2: 2248. Intersection of Multiple Arrays

Given a 2D array nums that contains n arrays of distinct integers, return a sorted array containing all the numbers that appear in all n arrays.

For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4]. 3 and 4 are the only numbers that are in all arrays.
```python
from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)
        for arr in nums:
            for x in arr:
                counts[x] += 1

        n = len(nums)
        ans = []
        for key in counts:
            if counts[key] == n:
                ans.append(key)
        
        return sorted(ans)
```

This problem is a good discussion point for why a hash map is convenient. You may be thinking, since our keys are integers, why can't we just use an array instead of a hash map? We could, but the problem is that the array needs to be at least as large as the maximum element. What if huge numbers could be in the input? What if we have a test case like [1, 2, 3, 1000]? We need to initialize an array of size 1000, even though only a few of the values will be updated. Therefore, using an array could end up being a huge waste of space. Sure, sometimes it would be more efficient because of the overhead of a hash map, but overall, a hash map is much safer. Even if 99999999999 is in the input, it doesn't matter - the hash map handles it like any other element.

Let's say that there n lists and each list has an average of m elements. To populate our hash map, it costs O(n⋅m) to iterate over all the elements. Then, there can be at most m elements inside ans when we perform the sort, which means in the worst case, the sort will cost O(m⋅logm). This gives us a time complexity of log O(n⋅m+m⋅logm)=O(m⋅(n+logm)). If every element in the input is unique, then the hash map will grow to a size of n⋅m, which means the algorithm has a space complexity of O(n⋅m).

```html
Example 3: 1941. Check if All Characters Have Equal Number of Occurrences

Given a string s, determine if all characters have the same frequency.
For example, given s = "abacbc", return true. All characters appear twice. Given s = "aaabb", return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.
```

Using our knowledge of hash maps and sets, this is a very straightforward problem. Use a hash map counts to count all character frequencies. Iterate through s and get the frequency of every character. Check if all frequencies are the same.

Because a set ignores duplicates, we can put all the frequencies in a set and check if the length is 1 to verify if the frequencies are all the same.

```python
from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        # {'a': 2, 'b':2, 'c': 2}
        frequencies = counts.values() 
        # after set of the counts values -> {2 ,2,2} -> {2}
        return len(set(frequencies)) == 1
```
Given n as the length of s, it costs O(n) to populate the hash map, then O(n) to convert the hash map's values to a set. This gives us a time complexity of O(n), and a space complexity of O(n) for both the hash map and set.

Bonus Python one liner using collection's [Counter](https://docs.python.org/3/library/collections.html#collections.Counter):

```python
from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1
```

### Count the number of subarrays with an "exact" constraint

In the sliding window article from chapter 1, we talked about a pattern "find the number of subarrays/substrings that fit a constraint". In those problems, if you had a window between left and right that fit the constraint, then all windows from x to right also fit the constraint, where left < x < right.

For this pattern, we will be looking at problems with stricter constraints, so that the property just mentioned is not necessarily true.

>For example, "Find the number of subarrays that have a sum less than k" with an input that only has positive numbers would be solved with sliding window. In this section, we would be talking about questions like "Find the number of subarrays that have a sum exactly equal to k".


At first, some of these problems seem very difficult. However, the pattern is very simple once you learn it, and you'll see how similar the code is for each problem that falls in this pattern. The general algorithm goes like this:

Declare a hash map that maps keys to integers.

* You will usually have to also initially set **counts[0] = 1**. We'll talk about this in a bit.
* Declare an answer variable and a **curr** variable.


>curr will track whatever the constraint metric is for the entire prefix at any given point in iteration. For example, let's say the problem wants subarrays with sum equal to k. The "constraint metric" is the sum. So as we iterate, at any given index i, curr will be the sum of the input up to and including i (a prefix sum).

* Iterate over the input. At each element:
    - Check the hash map for curr minus the constraint. Add this frequency to the answer variable.
    - Increment the value associated with the key equal to curr: counts[curr] += 1.
    - Update curr

>When we say "minus the constraint", this means whatever the problem's numeric constraint is. So if the problem asks for subarrays with sum equal to k, then you would check the hash map for curr - k.

```html
Example 4: 560. Subarray Sum Equals K
Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.
```
```python
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for num in nums:
            curr += num
            ans += counts[curr - k]
            counts[curr] += 1
    
        return ans
```
Let's talk about the intuition behind why the algorithm above works for this problem. Let's say we have nums = [1, 2, 1, 2, 1], k = 3. There are four subarrays with sum 3 - [1, 2] twice and [2, 1] twice.

Remember prefix sums? We learned that with a prefix sum, we can find the sum of any subarray from left to right by looking at the difference between their indices in the prefix sum. The prefix sum for this input, which is what curr represents, is [1, 3, 4, 6, 7]. **_Any difference between elements that is equal to 3 represents a subarray whose sum is equal to 3_**.
>中文解释：在prefixsum里的每个子集，如果子集-k的值存在于prefixsum的子集里，就说明了当前的子集集合== k.

At any index, **_if curr - k existed earlier as a prefix, then the subarray from that point and the current index has a sum of curr - (curr - k) = k_**. If we store all the prefixes in a hash map counts, we can query counts[curr - k] to find subarrays with sum equal to k.

We said there were four subarrays with sum 3, but there's only three differences in [1, 3, 4, 6, 7] of 3: 4 - 1, 6 - 3, and 7 - 4. What's wrong? Well, at the second index, the prefix is equal to 3, which is a valid subarray, but we are missing the 0. This is why in the first step of the general algorithm above, we need to initialize the hash map with 0: 1. Because technically, the empty subarray [] is a subarray with sum 0.

You may be thinking, if curr is only increasing, then no value in the hash map is greater than 1, couldn't we just use a set? This would be true if the array only had non-negative numbers - however, the constraints say -1000 <= nums[i] <= 1000. Let's think about an example: nums = [1, -1, 1, -1], k = 0. There are four valid subarrays: [1, -1] twice, [-1, 1] once, and the entire array [1, -1, 1, -1].

The prefix sum is [1, 0, 1, 0]. There are two subarrays ending on the final index - [1, -1] and the entire array. Remember that we initialize counts[0] = 1, so after the second index, we have counts[0] = 2. So when we reach the final index and do ans += counts[curr - k] = ans += counts[0], we are adding both subarrays to our answer. When there are negative numbers in the input, the same prefix can occur multiple times, and a hash map is needed to count the frequency.


To summarize:
- We use curr to track the prefix sum.
- At any index i, the sum up to i is curr. If there is an index j whose prefix is curr - k, then the sum of the subarray with elements from j + 1 to i is curr - (curr - k) = k.
- Because the array can have negative numbers, the same prefix can occur multiple times. We use a hash map counts to track how many times a prefix has occurred.
- At every index i, the frequency of curr - k is equal to the number of subarrays whose sum is equal to k that end at i. Add it to the answer.
The time and space complexity of this algorithm are both O(n), where n is the length of nums. Each for loop iteration runs in constant time and the hash map can grow to a size of n elements

>中文解释：在prefixsum里的每个子集，如果子集-k的值存在于prefixsum的子集里，就说明了当前的子集集合== k.

```html
Example 5: 1248. Count Number of Nice Subarrays

Given an array of positive integers nums and an integer k. Find the number of subarrays with exactly k odd numbers in them.

For example, given nums = [1, 1, 2, 1, 1], k = 3, the answer is 2. The subarrays with 3 odd numbers in them are [1, 1, 2, 1, 1] and [1, 1, 2, 1, 1].
```

```python
from collections import defaultdict
from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0
        
        for num in nums:
            curr += num % 2
            ans += counts[curr - k]
            counts[curr] += 1

        return ans
```

In the previous example, the constraint metric was a sum, so we had curr record a prefix sum. In this problem, the constraint metric is odd number count. Therefore, let's have curr track the number of odd numbers. At every element, we can query curr - k again. In the example test case, at the final index, curr = 4 because there are 4 odd numbers in the array. At the first index, curr = 1. 4 - 1 = 3, and you can see that the subarray from index 1 to 4 is one of the answers ([1, 1, 2, 1, 1]).

>We can check if a number is odd by taking it mod 2. If x is odd, then x % 2 = 1.