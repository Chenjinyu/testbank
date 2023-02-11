"""
Given n US dollars, write a method that returns an array of Euro denominations
that sum up to the converted value in Euros using the least number of bills and coins
"""


def coinChangeDSF(coins, amount):
    # DFS + Greedy
    coins = sorted(coins, reverse=True)
    min_number = float('inf')
    min_arr = [0] * (amount + 1)
    tmp_arr = min_arr

    min_arr = change_helper(coins, 0, amount, 0, min_number, min_arr)
    print(min_arr)
    return [] if min_arr == tmp_arr else min_arr


def change_helper(coins, start_pos, amount, count, min_number, min_arr):
    coin = coins[start_pos]
    # last element, eg: 1.
    if start_pos == len(coins) - 1:
        if amount % coin == 0:
            min_number = min(min_number, (count + amount // coin))
            min_arr = min(min_arr, [coin] * min(min_number, amount // coin), key=len)
    else:
        k = amount // coin
        # count is current count of coins which be included in.
        # count + k must less than min_number, otherwise, it's not the optimal answer.
        if k >= 0 and count + k < min_number:
            for i in range(k, -1, -1):
                min_arr = change_helper(coins, start_pos + 1, (amount - i * coin), (count + i), min_number, min_arr)
    return min_arr


coins = [1, 2, 5]
amount = 11
# print(coinChangeDSF(coins, amount))
#
#
# for i in range(10, -1, -1):
#     print(i)
