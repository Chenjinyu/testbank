"""
12. Integer to Roman
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together.
Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four. The same principle applies to the number nine,
which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: 3
Output: "III"

Example 2:
Input: 4
Output: "IV"

Example 3:
Input: 9
Output: "IX"

Example 4:
Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:
Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


class Solution:
    """
    Amazon OA Problem
    LinkedIn OA Problem
    Apple OA Problem
    """
    def intToRoman(self, num: int) -> str:
        roman_dict = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        res = ""
        num_list = list(roman_dict.keys())
        while num:
            for idx in range(len(roman_dict) - 1, -1, -1):
                if num - num_list[idx] >= 0:
                    num = num - num_list[idx]
                    res += roman_dict[num_list[idx]]
                    break

        return res


if __name__ == "__main__":
    """
    
    """
    testcases = [
        {'s': 3000, 'e': 'MMM'},
        {'s': 1994, 'e': 'MCMXCIV'},
        {'s': 1986, 'e': 'MCMLXXXVI'},
        {'s': 1600, 'e': 'MDC'},
        {'s': 1430, 'e': 'MCDXXX'},
        {'s': 60, 'e': 'LX'},
        {'s': 59, 'e': 'LIX'},
        {'s': 58, 'e': 'LVIII'},
        {'s': 9, 'e': 'IX'},
        {'s': 4, 'e': 'IV'},
        {'s': 3, 'e': 'III'},
    ]
    is_pass = True
    for case in testcases:
        actual_result = str(Solution().intToRoman(case['s']))
        print("Input: {}\nExpected: {}\nAcutal: {}\nis_Passed: {}".format(case['s'],
                                                                          case['e'],
                                                                          actual_result,
                                                                          actual_result == case['e']))
        if actual_result != case['e']:
            is_pass = False

    if not is_pass:
        print("!!!!-----FAILED------!!!!")
