"""
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.


Example 1:
Input: s = "ab-cd"
Output: "dc-ba"

Example 2:
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Constraints:
1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.
"""

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        """ Two Pointers Pattern is the good algorithm """
        s_arr = [None] * len(s)
        left, right = 0, len(s_arr) - 1
        # while left < right: if use this condition will raise error with None, since the s_arr need to be filed with the lenght of s.
        while left < len(s) and right >= 0:
            if not s[left].isalpha():
                s_arr[left] = s[left]
                left += 1
            elif not s[right].isalpha():
                s_arr[right] = s[right]
                right -= 1
            else:
                s_arr[left] = s[right]
                s_arr[right] = s[left]
                left += 1
                right -= 1
            
        return "".join(s_arr)
    
    
    def reverseOnlyLettersWithSplitStr(self, s: str) -> str:
        """
        My bad, I forgot the list(str) is convert string to list, should not use str.split() within/out delimiter.
        """
        s_arr = list(s)
        left, right = 0, len(s_arr) - 1
        # while left < len(s) and right >= 0: since the s_arr be filed from 0 to length of s. it will be switched twice, then its the same with orignal. 
        while left < right:
            if not s_arr[left].isalpha():
                left += 1
            elif not s_arr[right].isalpha():
                right -= 1
            else:
                s_arr[left], s_arr[right] = s_arr[right], s_arr[left]
                left += 1
                right -= 1
            
        return "".join(s_arr)
        
# print(Solution().reverseOnlyLetters("ab-cd"))
print(" A B ".split())
print(list("ab-cd"))