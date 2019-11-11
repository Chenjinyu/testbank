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