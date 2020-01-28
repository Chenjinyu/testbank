"""
Day of Week

Days of the week are represented as three-letter strings("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun").

Write a function solution that, given a string S representing the day of the week
and an integer K (between 0 and 500, inclusive), return the day of the week that is K days later.

Example:
     Given S = "Wed", and K = 2. the function should return "Fri".
     Given S = "Sat" and K = 23, the function should return "Min".

"""

def returnDayofWeek(S, K):
    day_of_week_list = [
        "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"
    ]

    value = day_of_week_list.index(S)

    _, new_value = divmod(value + K, 7)

    return day_of_week_list[new_value]


S = "Sat"
K = 23
print(returnDayofWeek(S, K))
