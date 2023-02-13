"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Example 1:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:
Input: sentence = "leetcode"
Output: false
 

Constraints:
1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""
from collections import Counter
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """
        This is very simple question, but there has many solutions
        1. Counter to get list(sentence), if the length of the keys equal to 26
        2. dictionary to insert all letter in the loops, and check the length of the keys.
        3. Set() to get all letters avoidng duplicates.
        """
        eng_letters="abcdefghijklmnopqrstuvwxyz"
        for letter in eng_letters:
            if letter not in sentence:
                return False
        return True
    
    
    def checkIfPangramSet(self, sentence: str) -> bool:
        # return set("abcdefghijklmnopqrstuvwxyz") == set(sentence)
        return len(set(sentence)) == 26
    
    def checkIfPangramCounter(self, sentence: str) -> bool:
        ht = Counter(sentence)
        return len(ht) == 26
    
        
test = "thequickbrownfoxjumpsoverthelazydog"
print(sorted(set(test)))