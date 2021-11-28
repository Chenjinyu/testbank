"""
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    """
    Amazon OA Problem.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time Complexity: O(len(s))
        """
        length = len(s)
        left, right = 0, 0
        charset = set()
        max_len = 0

        while right < length:
            if s[right] not in charset:
                charset.add(s[right])
                max_len = max(len(charset), max_len)
                right += 1
            else:
                charset.remove(s[right])
                left += 1
        return max_len

    def lengthOfLongestSubstringImprove(self, s: str) -> int:
        """
        Time Complexity: O(len(s))
        """
        max_len = 0
        max_length_chars = ''
        for x in s:
            if x in max_length_chars:
                max_length_chars += x
                # remove the old one. string.find() find the first index of matched char.
                max_length_chars = max_length_chars[max_length_chars.find(x) + 1:]
            else:
                max_length_chars += x
                # get the max length to max_len each time, so no matter how long find,
                # it will return the max len anyway.
                max_len = max(max_len, len(max_length_chars))
        return max_len

    def lengthOfLongestSubstringRound2(self, s: str) -> int:
        """
        Time Complexity: O(len(s)^2), the lengthOfLongestSubstringImprove and lengthOfLongestSubstringSolved 
        are the good solutions.
        """
        if not s: return 0
        l, r = 0, 0
        sliding_window = {}
        max_len = float("-inf")
        while r < len(s):
            sliding_window[s[r]] = sliding_window.get(s[r], 0) + 1
            # the second while here for moving left pos.
            # while must has two conditions. 
            while l < r and sliding_window[s[r]] == 2:
                sliding_window[s[l]] = sliding_window.get(s[l], 0) - 1
                l += 1
            max_len = max(max_len, r - l + 1)
            r += 1
        return len(s) if max_len == float("-inf") else max_len
    

if __name__ == "__main__":
    testcases = [
        {'s': "abcabcbb", 'e': '3'},
        {'s': "bbbbb", 'e': '1'},
        {'s': "pwwkew", 'e': '3'},
        {'s': "pweeewkew", 'e': '3'},
        {'s': "abcdefghijklmnopqrstuvwxyz", 'e': '26'},
        {'s': "", 'e': '0'},
        {'s': "dvdf", 'e': '3'},
        {'s': "tmmzuxt", 'e': '5'},
    ]
    # for case in testcases:
    #     actual_result = str(Solution().lengthOfLongestSubstringRound2(case['s']))
    #     print("Input: {}\nExpected: {}\nAcutal: {}\nis_Passed: {}".format(case['s'],
    #                                                                       case['e'],
    #                                                                       actual_result,
    #                                                                       actual_result == case['e']))

    print(4 ^ 2)
    print(pow(4, 2))
    print(4 ** 2)
