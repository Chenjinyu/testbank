"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"

Constraints:
1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        """
        reversed(lst) retruns an iterator that yields items in reverse order
        """
        s_word_lst = s.split(" ") # time complexity is O(N)
        revesrsed_str = ""
        for word in s_word_lst:
            revesrsed_str += " " + "".join(reversed(word))
            
        return revesrsed_str[1:]
    
    
    def reserseWordsSimple(self, s: str) -> str:
        """
        Time Complexity is O(N)
        list[::-1] equals to list[:None:-1] and list[:len(list)-1: -1] reverse list to a new list
        """
        return ' '.join([substring[::-1] for substring in s.split(' ')])
