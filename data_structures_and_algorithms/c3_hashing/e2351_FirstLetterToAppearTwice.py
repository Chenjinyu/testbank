"""
Given a string s consisting of lowercase English letters, return the first letter to appear twice.

Note:
A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
s will contain at least one letter that appears twice.
 

Example 1:
Input: s = "abccbaacz"
Output: "c"
Explanation:
The letter 'a' appears on the indexes 0, 5 and 6.
The letter 'b' appears on the indexes 1 and 4.
The letter 'c' appears on the indexes 2, 3 and 7.
The letter 'z' appears on the index 8.
The letter 'c' is the first letter to appear twice, because out of all the letters the index of its second occurrence is the smallest.

Example 2:
Input: s = "abcdd"
Output: "d"
Explanation:
The only letter that appears twice is 'd' so we return 'd'.
 

Constraints:
2 <= s.length <= 100
s consists of lowercase English letters.
s has at least one repeated letter.
"""
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        s_dict = {}
        for idx, val in enumerate(s):
            # val in s_dict equals val in s_dict.keys()
            if val not in s_dict:
                s_dict[val] = 1
            else:
                return val
            
    def repeatedCharacterSet(self, s: str) -> str:
        """
        Time Complexity: O(N)
        Space Complexity: O(M)
        The space complexity is a more interesting topic of discussion. Many people will argue that the space complexity is O(1) because the input can only have characters from the English alphabet, which is bounded by a constant (26). This is very common with string problems and technically correct. In an interview setting, this is probably a safe answer, but you should also note that the space complexity could be O(m), where m is the number of allowable characters in the input.
        """
        seen = set()
        for c in s:
            if c in seen:
                return c
            seen.add(c)
        return " "
            
            
test_dict = {'Jinyu': 'Chen', 'Yuning': 'Chen'}
print("Chen" in test_dict) # False
print("Jinyu" in test_dict) # True