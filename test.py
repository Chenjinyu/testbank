# nums = [1, 2, 3, 45, 5]
# N = len(nums)
# print(list(range(N, 0, -1)))
# print("-----")
# print(nums[::-1])
#
# def multipy(a:tuple):
#     return a[0] * a[1]
#
# print(list(map(sum, zip([1, 2, 3], [4, 5, 6]))))
# print(list(map(multipy, zip([1, 2, 3], [4, 5, 6]))))
#
# i = 0
# for i in range(10):
#     print(i)
#     i += 2
#
# val1 = 4
# val2 = 3
# result_list = []
# result_list.extend([2] * min(val1,val2))
# print(result_list)
#
# test = [1, 2, 3, 1]
# print(test[-2])
# print('----')
# # print(test.index(1))
#
# # for val in test:
# #     print(val)
# #     test.remove(1)
# print('----')
# index = 0
# while index < len(test):
#     print(test[index])
#     if test[index] == 1:
#         test.remove(test[index])
#     else:
#         index += 1
#
# print("--------------line-------------")
# board = \
#     [
#         ["5", "3", "9", ".", "7", ".", ".", ".", "."],
#         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#         [".", "9", "8", ".", ".", ".", ".", "6", "."],
#         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#         [".", "6", ".", ".", ".", ".", "2", "8", "."],
#         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#         [".", ".", ".", ".", "8", ".", ".", "7", "9"]
#     ]
#
# z_list_1 = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
# z_list_2 = [["2", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
# z_list_3 = [["3", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
#
# result = zip(z_list_1, z_list_2, z_list_3)
# result = []
# for index in range(len(board)):
#     result.append([board[index][0:3], board[index][3:6], board[index][6:9]])
# zip_result = []
# for zip_time in [0, 3, 6]:
#     zip_result.extend(zip(result[zip_time], result[zip_time + 1], result[zip_time + 2]))
#
# for v in zip_result:
#     print(v)
#     v_result = v[0] + v[1] + v[2]
#     print(v_result)
#     print("-------")
#     v_result = [val for val in v_result if val != "."]
#     print(v_result)
#     # if len(v_result) > len(set(v_result)):

#
# print(list(result))
# print(list(zip_result))
import collections
# def isValidSudoku(board):
#     seen = sum(([(c, i), (j, c), (i / 3, j / 3, c)]
#                 for i, row in enumerate(board)
#                 for j, c in enumerate(row)
#                 if c != '.'), [])
#
#     return len(seen) == len(set(seen))
#
# # print(isValidSudoku(board))
#
# for i, row in enumerate(board):
#     print(str(i), row)
#     for j, c in enumerate(row):
#         print(str(j), c)
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# result = [(7, 4, 1), (8, 5, 2), (9, 6, 3)]
# print(matrix[~1][~2])
# print(matrix[1][2])
# print(matrix[::-1])

# from collections import Counter
# test = Counter(["A","A","A","B","B","C","C","D","D","E","F","G","H"])
# test2 = Counter(["B","A","B","A","B","C","C","D","D","E","F","G","H"])
# print(test == test2)
#
# print(15//2)
# float_test = "4.21"
# print(float(float_test))
# test = "1.0"
# print(float_test.isdigit()) # digit, any number from 0 - 9
# print(max(-2 ** 31, -91283472332))
#
# print('test'[0:1])
# strs = ["ought", "thought", "think", "fourth", "the"]
# strs = sorted(strs, key=len)
# print(strs)
# import functools
# print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))

# d = {}
#
#
# d["k"] = 6
#
# d["k"] += 1
#
# print(d["k"])  # 7
#
# from collections import defaultdict
#
# d = defaultdict(str)
# d["k"] += "1"
#
# print(d["k"])

# test = [1,3,-1,-3,5,3,6,7]
# print(test[5:len(test)])
# print(sum(test[0:3]))
# print(test[4:4])
#
# import itertools
# print(list(itertools.accumulate(test)))
#
# print(list(range(0, 2)))

from collections import Counter
# P = [0,1,3,2,4,0]
# print(0 in P)
# print(P.index(0))
# print(sorted(P))
# print(P[::-1])
# print(P)
# print(9**0.5)
# import math
# print(round(math.log(26, 3), 9))
# print(round(math.log(26, 3)))
# print(27%3)
# print(str(190).zfill(8))
# print('{:<08d}'.format(190))
# print('{:>08d}'.format(190))
# test = -0
# print(test in P)
#
# print(list(range(5, 2, -1)))
# print(list(range(1,5)))
# print(list(range(1,1)))
#
# test = "123"
# print(test[::-1])
#
# print(divmod(10, 10))
#
# test = ["chen", "jinyu", "love"]
# print(test[::-1])
#
# forwardRouteList = [[1, 3000], [2, 5000], [3, 7000], [4, 10000]]
# print(dict(forwardRouteList))
# log = "dig1 8 1 5 1"
# print(log.split(" ", 1))
# test = ["Jin", "Chen", "yu"]
# print(sorted(test, key=len))
# print("-----")
# from heapq import heappush, heappop, heapify
# heap = []
# data = [(1, 'J'), (4, 'N'), (3, 'H'), (2, 'O')]
# heapify(data)
#
# while data:
#     print(heappop(data))
# char = 'a'
# print(ord(char))

# from collections import namedtuple
# Point = namedtuple('Pointxx', ['x', 'y'])
# p = Point(11, y=22)
# print(p.x)
# print(Point.__doc__)

# from collections import defaultdict
# test = defaultdict(list)
# test[1].append(2)
# test[1].append(3)
# print(test)
#
# class Solution:
#     def fib(self, n: int) -> int:
#         cached = defaultdict(int)
#         return self.memoize(n, cached)
#
#     def memoize(self, n: int, cached):
#         if n <= 1: return n
#         elif cached[n] > 0:
#             return cached[n]
#
#         cached[n] = self.memoize(n - 1, cached) + self.memoize(n - 2, cached)
#         return cached[n]
#
#
# if __name__ == "__main__":
#     print(Solution().fib(8))
#
# def test(i,j):
#     return i,j
#
# print(eval('test')(1,2))
#
# test = " test "
# print(test.strip())
import functools
#
# mod_first, mod_rest = divmod(994, 500)
# print(mod_first, mod_rest)
# print(functools.reduce(lambda a, b: a - b, test[::-1]))
# from functools import reduce
# test = [1,2,3,4]
# for idx in range(len(test)):
#     print(reduce(lambda x, y: x * y, [x for i, x in enumerate(test) if idx != i]))

# test = [[4,17], [4,6],[4,8], [4,5]]
# test.sort(key=lambda x: x[0])
# print(test)

import heapq


import math
# print(math.pow(62, 6))
# # 56,800,235,584
# #52,036,560,683,837,095,936
# # 5.20365606838371e+19
#
# test = [1,1,1,2,2]
# print(test.count(1))
#
#
# # inorder traversal
#
# def inorderTraversal(root):
#     res = []
#     stack = []
#     cur = root
#
#     while root or cur:
#         while cur:
#             stack.append(cur)
#             cur = cur.left
#
#         cur = stack.pop()
#         res.append(cur.val)
#         cur = cur.right
#
#     return res
# print(5.0//2.0)
# print(5//2)
# print(5%2)
# print(divmod(5,2))

import logging


def multiply(x):
    return (x * x)


def add(x):
    return (x + x)


funcs = [multiply, add]
for i in range(5):
    # map(fun, iter)
    value = map(lambda x: x(i), funcs)
    print(list(value))

#
# def test_fun():
#     logging.info('in test module')



# test = [1,2,3,4]
# print(test.index(5))

numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

# Notice, the size of numbersList and numbers_tuple is different
result1 = zip(numbersList, numbers_tuple)
print(result1)
# Converting to set
result_set1 = set(result1)
print(result_set1)

result2 = zip(numbersList, str_list, numbers_tuple)

# Converting to set
result_set = list(result2)
print(result_set)
n, s, t = zip(*result_set)
print('n ->', n)
print('n ->', s)
print('n ->', t) # convert to set.

