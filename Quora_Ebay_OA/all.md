### [Quora and Ebay OA](#Quora-and-Ebay-OA)

- [1. product sum](#product-sum)
- [2. valid word](#valid-word)
- [3. compare string](#compare-string)
- [4. cool feature](#cool-feature)
- [5. find even digit](#find-even-digit)
- [6. find most common](#find-most-common)
- [7. maximum size of ribbon](#maximum-size-of-ribbon)
- [8. good tuple](#good-tuple)
- [9. rotate matrix among diagonal](#rotate-matrix-among-diagonal)
- [10. is prefix](#is-prefix)
- [11. max arithmetic length](#max-arithmetic-length)
- [12. divide substring](#divide-substring)
- [13. sum of substring](#sum-of-substring)
- [14. query interval count](#query-interval-count)
- [15. find min of matrix](#find-min-of-matrix)
- [16. reverse digits in pairs](#reverse-digits-in-pairs)
- [17. longest equal subarray](#longest-equal-subarray)
- [18. frame window](#frame-winodw)
- [19. remove exactly one digit](remove-exactly-one-digit)
- [20. covering segments by points](#covering-segments-by-points)
- [21. counting out rhymes](#counting-out-rhymes)
- [22. max sum square submatrix](#max-sum-square-submatrix)
- [23. sort diagonal](#sort-diagonal)
- [24. binary pattern matching](#binary-pattern-matching)
- [25. find target in window](#find-target-in-window)

#### product sum
```python
"""
Product Sum
Input: 230
Output: -6
Explanation: 2 * 3 * 0 - (2 + 3 + 0) = -5
"""


def product_sum(num):
    product = 1
    addition = 0
    while num:
        i = num % 10
        product *= i
        addition += i
        num //= 10
    return product - addition


num = 230
print(product_sum(num))
```

[Go Top](#Quora-and-Ebay-OA)

#### valid word
```python
"""
Valid Word
Input:
words = ["hEllo##", "This^^"]
letters = ["h", "e", "l", "o", "t", "h", "s"]
Output: 1
Explanation: hEllo## is a valid word, This^^ is not a valid word (ignore symbol)
"""


def valid_word(words, letters):
    result = 0
    for word in words:
        word = [c for c in word if c.isalpha()]
        count = 0
        for c in word:
            if c.lower() in letters:
                count += 1
        if count == len(word):
            result += 1
    return result


words = ["hEllo##", "Ths^^"]
letters = ["h", "e", "l", "o", "t", "h", "s"]
print(valid_word(words, letters))
```

[Go Top](#Quora-and-Ebay-OA)

#### compare string
```python
"""
Compare the String with Frequency
Input: S1 = "babzccc", S2 = "abbzczz" Output: True
Explanation:
Count_S1 = {"a":1, "z":1, "b":2, "c":3}
Count_S2 = {"a":1, "c":1, "b":2, "z":3}
"""
from collections import Counter


def compare_string(S1, S2):
    count1 = Counter(S1)
    count2 = Counter(S2)
    if sorted(list(count1.keys())) != sorted(list(count2.keys())):
        return False
    if sorted(list(count1.values())) != sorted(list(count2.values())):
        return False

    return True


S1 = "babzccc"
S2 = "abbzczz"
print(compare_string(S1, S2))

S1 = "babzcccm"
S2 = "bbazzczl"
print(compare_string(S1, S2))
```

[Go Top](#Quora-and-Ebay-OA)

#### cool feature
```python
"""
Cool Feature
Give three array a, b and query. This one is hard to explain. Just read the example.
Input:
a = [1, 2, 3]
b = [3, 4]
query = [[1, 5], [1, 1, 1], [1, 5]]
Output: [2, 1]
Explain:
Just ignore every first element in sub array in query.
So we will get a new query like this query = [[5], [1, 1], [5]]
Only record the result when meet the single number in new query array.
And the rule of record is find the sum of the single number.
The example above is 5 = 1 + 4 and 5 = 2 + 3, there are two result.
So currently the output is [2]
When we meet the array length is larger than 1, such as [1, 1].
That means we will replace the b[x] = y, x is the first element, y is second element.
So in this example, the b will be modify like this b = [1, 4]
And finally, we meet the [5] again. So we will find sum again. This time the result is 5 = 1 + 4.
So currently the output is [2, 1]
note: Don't have to modify the query array, just ignore the first element.
"""

def cool_features(a, b, querys):
    res = []
    for q in querys:
        if len(q) == 3:
            b[q[1]] = q[2]
        else:
            q = q[1]
            count = 0
            for i in a:
                if q - i in b:
                    count += 1
            res.append(count)

    return res


a = [1, 2, 3]
b = [3, 4]
querys = [[1, 5], [1, 1, 1], [1, 5]]
print(cool_features(a, b, querys))
```


[Go Top](#Quora-and-Ebay-OA)

#### find even digit
```python
"""
Find Even Digit
Find how many numbers have even digit in a list
Input: A = [12, 3, 5, 3456]
Output: 2
"""
def find_even_digit(A):
    return len([a for a in A if a % 2 == 0])

A = [12, 3, 5, 3456]
print(find_even_digit(A))
```


[Go Top](#Quora-and-Ebay-OA)

#### find most common
```python
"""
Find Most Common
Input: A = [2, 2, 3, 3, 5]
Output: [2, 3]
"""

from collections import Counter

def find_most_common(A):
    counter_a = Counter(A)
    # get the maximum count
    most_common_count = max(counter_a.values())
    # get how many maximum it has
    count_common = list(counter_a.values()).count(most_common_count)
    return [val[0] for val in counter_a.most_common(count_common)]

A = [2, 2, 3, 3, 5]
print(find_most_common(A))
```


[Go Top](#Quora-and-Ebay-OA)

#### maximum size of ribbon
```python
"""
Given an int array wood representing the length of n pieces of wood and an int k.
It is required to cut these pieces of wood such that more or equal to k pieces of the same length len are cut.
What is the longest len you can get?

Example 1:

Input: wood = [5, 20, 7], k = 3
Output: 5
Explanation:
5 -> 5
9 -> 5 + 4
7 -> 5 + 2
Example 2:

Input: wood = [5, 9, 7], k = 4
Output: 4
Explanation:
5 -> 4 + 1
9 -> 4 * 2 + 1
7 -> 4 + 3
Example 3:

Input: wood = [1, 2, 3], k = 7
Output: 0
Explanation: We cannot make it.
Example 4:

Input: wood = [232, 124, 456], k = 7
Output: 114
Explanation: We can cut it into 7 pieces if any piece is 114 long,
however we can't cut it into 7 pieces if any piece is 115 long.
"""

def cut_wood(wood, k):
    res = 0
    left, right = 0, max(wood)

    def cut_helper(A, k, num):
        count = 0
        for a in A:
            count += a // num
        return count >= k

    while left <= right:
        mid = left + (right - left) // 2
        if cut_helper(wood,k, mid):
            res = max(mid, res)
            left = mid + 1
        else:
            right = mid - 1

    return res


wood = [5, 46, 7]
k = 3
print(cut_wood(wood, k))

```

[Go Top](#Quora-and-Ebay-OA)

#### good tuple
```python
"""
Good Tuples
Give an array and find the count of a pair number and a single number combination in a row of this array.
Target array is: a[i - 1], a, a[i + 1]
Input: a = [1, 1, 2, 1, 5, 3, 2, 3]
Output: 3
Explain:
[1, 1, 2] -> two 1 and one 2(O)
[1, 2, 1] -> two 1 and one 2(O)
[2, 1, 5] -> one 2, one 1 and one 5(X)
[1, 5, 3] -> (X)
[5, 3, 2] -> (X)
[3, 2, 3] -> (O)
different characters
intput: a = "aabdcreff"
output: 5
"""

def good_tuples(a):
    res = 0
    def checker(a, b, c):
        return len(set([a, b, c])) == len([a, b, c])

    for i in range(len(a) - 2):
        if checker(a[i], a[i + 1], a[i + 2]):
            res += 1
    return res

a = "aabdcreff"
print(good_tuples(a))
```

[Go Top](#Quora-and-Ebay-OA)

#### rotate matrix among diagonal

[Go Top](#Quora-and-Ebay-OA)

#### is prefix

[Go Top](#Quora-and-Ebay-OA)
#### max arithmetic length

[Go Top](#Quora-and-Ebay-OA)
#### divide substring

[Go Top](#Quora-and-Ebay-OA)
#### sum of substring

[Go Top](#Quora-and-Ebay-OA)
#### query interval count

[Go Top](#Quora-and-Ebay-OA)
#### find min of matrix

[Go Top](#Quora-and-Ebay-OA)
#### reverse digits in pairs

[Go Top](#Quora-and-Ebay-OA)
#### longest equal subarray

[Go Top](#Quora-and-Ebay-OA)
#### frame window

[Go Top](#Quora-and-Ebay-OA)
#### remove exactly one digit

[Go Top](#Quora-and-Ebay-OA)
#### covering segments by points

[Go Top](#Quora-and-Ebay-OA)
#### counting out rhymes

[Go Top](#Quora-and-Ebay-OA)
#### max sum square submatrix

[Go Top](#Quora-and-Ebay-OA)
#### sort diagonal

[Go Top](#Quora-and-Ebay-OA)
#### binary pattern matching

[Go Top](#Quora-and-Ebay-OA)
#### find target in window

[Go Top](#Quora-and-Ebay-OA)