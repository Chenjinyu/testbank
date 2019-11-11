### [#Quora-and-Ebay-OA]

- [product sum](#product-sum)
- [valid word](#valid-word)
- [compare string](#compare-string)
- [cool feature](#cool-feature)
- [find even digit](#find-even-digit)
- [find most common](#find-most-common)
- [maximum size of ribbon](#maximum-size-of-ribbon)

#product_sum
```python
"""
Product Sum
Input: 230
Output: -6
Explaination: 2 * 3 * 0 - (2 + 3 + 0) = -5
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


```python
"""
Valid Word
Input:
words = ["hEllo##", "This^^"]
letters = ["h", "e", "l", "o", "t", "h", "s"]
Output: 1
Explaination: hEllo## is a valid word, This^^ is not a valid word (ignore symbol)
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

```python
"""
Compare the String with Frequency
Input: S1 = "babzccc", S2 = "abbzczz" Output: True
Explaination:
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