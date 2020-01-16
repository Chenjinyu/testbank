"""
1. return max sum values from [1,2,4,1,7,8,3], the list could not select the neighboring.
eg. choose 1, could not choose 2, only can choose 4,1,etc.

OPT[i] = max(OPT[i - 2] + list[i], OPT[i - 1])
OPT[0] = list[0]
OPT[1] = max(list[0], list[1])
"""
arr = [1,2,4,1,7,8,3]
num = len(arr) - 1
def rec_opt(arr, num):
    if num == 0:
        return arr[0]
    elif num == 1:
        return max(arr[0], arr[1])
    else:
        choose_cur = rec_opt(arr, num - 2) + arr[num]
        not_choose_cur = rec_opt(arr, num - 1)
        return max(choose_cur, not_choose_cur)

print(rec_opt(arr, num))

import numpy as np

def dp_opt(arr, num):
    opt = np.zeros(len(arr))
    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])

    for i in range(2, len(arr)):
        choose_cur = opt[i - 2] + arr[i]
        not_choose_cur = opt[i - 1]
        opt[i] = max(choose_cur, not_choose_cur)

    return int(opt[num])

print(dp_opt(arr, num))


"""
2. arr = [3, 34, 4, 12, 5, 2], target = 9.
find the sum of arr equals to target. if find return True, otherwise return False

"""
arr = [3, 34, 4, 12, 5, 2]
target = 9
def rec_subset(arr, i, target):
    if target == 0:
        return True
    elif i == 0:
        return arr[i] == target
    elif arr[i] > target:
        return rec_subset(arr, i - 1, target)
    else:
        choose_cur = rec_subset(arr, i - 1, target - arr[i])
        not_choose_cur = rec_subset(arr, i - 1, target)
        return choose_cur or not_choose_cur

print(rec_subset(arr, len(arr) - 1, target))

"""
对于dp，最主要的是要找到出口，也就是能最终决定的地方。像 if target == 0: return True
    target 0  1  2  3  4  5  6  7  8  9
arr   
3     0    F  F  F  T  F  F  F  F  F  F
34    1    T
4     2    T
12    3    T
5     4    T
2     5    T                    return here
 
"""


def dp_subset(arr, target):
    subset = np.zeros((len(arr), target + 1), dtype=bool)
    subset[:, 0] = True
    subset[0, :] = False
    subset[0, arr[0]] = True

    for i in range(1, len(arr)):
        for s in range(1, target + 1):
            if arr[i] > s:
                subset[i, s] = subset[i - 1, s]
            else:
                A = subset[i - 1, s - arr[i]]
                B = subset[i - 1, s]
                subset = A or B
    r, c = subset.shape
    return subset[r - 1, c - 1]

print(dp_subset(arr, target))

