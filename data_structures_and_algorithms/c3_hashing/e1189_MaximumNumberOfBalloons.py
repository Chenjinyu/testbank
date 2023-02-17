"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
"""
import math
from collections import Counter, defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloons_counter = Counter('balloon')
        for t in text:
            if t in balloons_counter.keys():
                balloons_counter[t] += 1
        
        min_single_char = min(balloons_counter.values()) - 1
        # min_double_chars = min(balloons_counter['l'], balloons_counter['o']) / 2 - 1
        # return math.floor(min(min_single_char, min_double_chars))
        # // operator is the floor division equals math.floor()
        min_double_chars = min(balloons_counter['l'], balloons_counter['o']) // 2 - 1
        return min(min_single_char, min_double_chars)
       
        
        
# // operator is the floor division        
print(5//2)