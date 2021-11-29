"""
Max Possible Value

Write a function solution that, given an integer N, returns the maximum possible value obtained
by inserting one '5' digit inside the decimal representation of integer N.

Example:
    1. Given N = 268, the function should return 5268.
    2. Given N = 670, the function should return 6750.
    3. Given N = 0, the function should return 50.
    4. Given N = -999, the function should return -5999.
Assume that:
    * N is an integer within the range [-8,000..8,000]

In your solution, focus on correctness, the performance of your solution will not be the focus of the assessment.
"""

def max_possible_value(N):
    sign = 1 if N >= 0 else -1
    N = str(N)
    if '-' in N:
        N = N[1:]

    for idx, val in enumerate(N):
        if sign == 1:
            if int(val) < 5:
                return int(N[0:idx] + str(5) + N[idx:])
        elif sign == -1:
            if int(val) > 5:
                return -int(N[0:idx] + str(5) + N[idx:])

# def max_possible_value2(N):
#     sign = 1 if N >= 0 else -1
#     N = str(N)
#     if '-' in N:
#         N = N[1:]
#     tmp = 10 * len(str(N))
#     while N:
#         if N < 10:
#             if sign > 0 and N < 5:
#                 return tmp * 10 + N
#             elif sign < 0 and N > 5:
#                 return (tmp * 10 + N) * sign
#         else:
#             first, rest = divmod(N, 10)
#             if sign > 0 and first < 5:
#                 return tmp * 5 + first * tmp / 10 + rest
#             elif sign < 0 and N > 5:
#                 return (tmp * 10 + N) * sign



N = [268, 670, 0, -999]
for n in N:
    print([(k, v) for k, v in enumerate(str(n))])
    print(max_possible_value(n))

