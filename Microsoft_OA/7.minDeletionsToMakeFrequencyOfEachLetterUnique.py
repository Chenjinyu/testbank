"""
Min Deletions to Make Frequency of Each Letter Unique

Given a string s consisting of n lowercase letters, you have to delete the minimum number of characters from s
so that every letter in s appears a unique number of times. We only care about the occurrences of letters that appear
at least once in result.


Example 1:
Input: "eeeeffff"
Output: 1
Explanation:
We can delete one occurence of 'e' or one occurence of 'f'.
Then one letter will occur four times and the other three times.

Example 2:
Input: "aabbffddeaee"
Output: 6
Explanation:
For example, we can delete all occurences of 'e' and 'f' and one occurence of 'd' to obtain the word "aabbda".
Note that both 'e' and 'f' will occur zero times in the new word, but that's fine,
since we only care about the letter that appear at least once.

Example 3:
Input: "llll"
Output: 0
Explanation:
There is no need to delete any character.

Example 4:
Input: "example"
Output: 4
"""

from collections import Counter


class Solution:
    def min_deletion(self, S: str) -> int:
        str_counter = Counter(S)
        unique_list = []
        rm_count = 0
        for val in str_counter.values():
            if val in unique_list:
                tmp = int(val) - 1
                if tmp > 0 and tmp not in unique_list:
                    unique_list.append(tmp)
                    rm_count += 1
                else:
                    rm_count += val
            else:
                unique_list.append(val)
        return rm_count


if __name__ == "__main__":
    testcases = [
        {'s': "eeeeffff", 'e': '1'},
        {'s': "aabbffddeaee", 'e': '6'},
        {'s': "llll", 'e': '0'},
        {'s': "example", 'e': '4'},
    ]
    for case in testcases:
        actual_result = str(Solution().min_deletion(case['s']))
        print("Input: {}\nExpected: {}\nAcutal: {}\nis_Passed: {}".format(case['s'],
                                                                          case['e'],
                                                                          actual_result,
                                                                          actual_result == case['e']))
