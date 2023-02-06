"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Example 4:
Input: ransomNote ="aab", magazine = "baa"
output: true

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""
import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = collections.Counter(magazine)
        magazine_dict_keys = magazine_dict.keys()
        ransonNote_dict = collections.Counter(ransomNote)
        for note_letter, note_count in ransonNote_dict.items():
            if note_letter not in magazine_dict_keys:
                return False
            elif note_count > magazine_dict[note_letter]:
                return False
        return True
    
    
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        return not(collections.Counter(ransomNote) - collections.Counter(magazine))
    
    