"""
Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "".join([val.lower() for val in s if val not in string.punctuation and val not in string.whitespace]).strip()
        # pos = len(s) // 2
        # return s[:pos] == s[len(s) - pos:len(s)][::-1]
        # s = [val.lower() for val in s if val not in string.punctuation and val not in string.whitespace]
        s = [val.lower() for val in s if val.isalnum()]
        return s == s[::-1]

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))