"""
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = left = 0
        sub_str_dic = defaultdict(int)
        for right in range(len(s)):
            if s[right] in sub_str_dic:
                # getting the max one since the new substring window starts
                left = max(left, sub_str_dic[s[right]] + 1)
            sub_str_dic[s[right]] = right    
            ans = max(ans, right - left + 1)
        return ans
            

print(Solution().lengthOfLongestSubstring("pwwkew"))
            