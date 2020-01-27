"""
Given two strings as input.
str1 => binary (consists 1/0)
str2 => consists A/B's
Also, 0 represents ONE/more A's
1 might represent ONE/more A's (or) one/more B's
Find if str2 matches str1 (based on the conditions specified) and return True/False

Example 1:
i/p:
str1 = 0100
str2 = AABBBAAA
o/p:
True
Explanation:
First 0 of str1 can match 2 initial A's of str2. The next 1 can match the following 3 B's.
The next 0 of str1 can match the following 1 A and the final 0 of str1 can match the last 2 A's of str2.

Example 2:
i/p:
str1 = 0011
str2 = AAB
o/p:
False
Explanation:
Each char of str1 must represent atleast ONE or more characters in str2. Here the length of str2 is less than str1.
Hence False.

Example 3:
i/p:
str1 = 01011
str2 = AAAABBBB
o/p:
True
Explanation:
The first 3 chars of str1 "010" can represent the initial "AAAA" of str2 and the following "11" of str1
can represent "BBBB" of str2 and hence condition is satisfied => True is returned
"""

def string_pattern_matching(str1, str2):
    pass


if __name__ == "__main__":
    testcases = [
        {'str1': '0100', 'str2': 'AABBBAAA', 'e': True},
        {'str1': '0011', 'str2': 'AAB', 'e': False},
        {'str1': '01011', 'str2': 'AAAABBBB', 'e': True},
    ]
    for case in testcases:
        actual_result = string_pattern_matching(case['str1'], case['str2'])
        print("Input: {}\nExpected: {}\nAcutal: {}\nis_Passed: {}".format(case['str1'],
                                                                          case['e'],
                                                                          actual_result,
                                                                          actual_result == case['e']))
