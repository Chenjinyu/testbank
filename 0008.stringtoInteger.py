"""
String to Integer (atoi)

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.

Problem Solving:
1. string.isdigit() is the function to check if the string is a integer.
2. in the begin of string, once strip(), don't care about whitespace anymore.
3. at the begin, it will have +, -, 0. out of the loop, check the first char if it's sign.
4. in the loop, calculate the result in the loop is a good way to go. because if still has a sign, the result is 0.
5. also if the result still 0, second 0 shows up, script will ignore.
6. if the result is not 0, second 0 shows up, it should be added into.
"""


class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if not str:
            return 0

        result = 0
        sign = 1
        start = 0
        if str[start] in ['-', '+']:
            if str[start] == '-':
                sign = -1
            start += 1

        for c in str[start:]:
            if c == '0' and result == 0:
                continue

            if not c.isdigit():
                break

            result = result * 10 + int(c)

        result = result * sign
        if result > 0:
            return min(result, 2 ** 31 - 1)
        else:
            return max(-2 ** 31, result)


if __name__ == "__main__":
    testcases = [
        {'s': " 0-1 ", 'e': '0'},
        {'s': "  0000001 ", 'e': '1'},
        {'s': "  ---  ", 'e': '0'},
        {'s': "  +++  ", 'e': '0'},
        {'s': "  +-2  ", 'e': '26'},
        {'s': "-5-", 'e': '0'},
        {'s': "-3.134", 'e': '3'},
        {'s': "43", 'e': '43'},
        {'s': "-91283472332", 'e': '-2147483648'},
        {'s': "+1", 'e': '1'},
        {'s': "010", 'e': '10'},
    ]
    for case in testcases:
        actual_result = str(Solution().myAtoi(case['s']))
        print("Input: {}\nExpected: {}\nAcutal: {}\nis_Passed: {}".format(case['s'],
                                                                          case['e'],
                                                                          actual_result,
                                                                          actual_result == case['e']))
