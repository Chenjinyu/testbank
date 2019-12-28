"""
273.Integer to English Words
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""


class Solution:
    """
    High Frequency!!!
    Facebook OA Problem
    Amazon OA Problem
    Microsoft OA Problem
    LinkedIn OA Problem
    Google OA Problem
    """
    def numberToWords(self, num: int) -> str:
        def less_ten(num):
            switcher = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
            return switcher.get(num)

        def less_twenty(num):
            switcher = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
            return switcher.get(num)

        def ten(num):
            switcher = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return switcher.get(num)

        def two(num):
            if not num: return ''
            elif num < 10:
                return less_ten(num)
            elif num < 20:
                return less_twenty(num)
            else:
                tenner, rest = divmod(num, 10)
                return ten(tenner) + ' ' + less_ten(rest) if rest else ten(tenner)

        def three(num):
            hundred, rest = divmod(num, 100)
            if hundred and rest:
                return less_ten(hundred) + ' Hundred ' + two(rest)
            elif not hundred and rest:
                return two(rest)
            elif hundred and not rest:
                return less_ten(hundred) + ' Hundred'

        billion, rest_m = divmod(num, 1000000000)
        million, rest_t = divmod(rest_m, 1000000)
        thousand, rest = divmod(rest_t, 1000)

        if not num:
            return 'Zero'

        result = ''
        if billion:
            result += ' ' if result else ''
            result += three(billion) + ' Billion'
        if million:
            result += ' ' if result else ''
            result += three(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += three(thousand) + ' Thousand'
        if rest:
            result += ' ' if result else ''
            result += three(rest)

        return result


if __name__ == "__main__":
    # test = 1234567891
    # div_frist, div_sencond = divmod(test, 1000000000)
    # print(div_frist, div_sencond)
    # div_first_2, div_second_2 = divmod(div_sencond, 1000000)
    # print(div_first_2, div_second_2)
    # div_first_3, div_second_3 = divmod(div_sencond, 1000)
    # print(div_first_3, div_second_3)

    testcases = [
        {'s': 100, 'e': 'One Hundred'},
        {'s': 123, 'e': 'One Hundred Twenty Three'},
        {'s': 143, 'e': 'One Hundred Forty Three'},
        {'s': 12345, 'e': 'Twelve Thousand Three Hundred Forty Five'},
        {'s': 1234567, 'e': 'One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven'},
        {'s': 1234567891,
         'e': 'One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One'},
    ]
    is_pass = True
    for case in testcases:
        actual_result = str(Solution().numberToWords(case['s']))
        print("Input: {}\nExpected: {}\nAcutal: {}\nis_Passed: {}".format(case['s'],
                                                                          case['e'],
                                                                          actual_result,
                                                                          actual_result == case['e']))
        if actual_result != case['e']:
            is_pass = False

    if not is_pass:
        print("!!!!-----FAILED------!!!!")