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