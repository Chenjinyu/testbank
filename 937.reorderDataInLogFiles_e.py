"""
937. Reorder Data in Log Files
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier. Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.
It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.
The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.
The digit-logs should be put in their original order.

Return the final order of the logs.


Example 1:
Input: logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]


Constraints:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
"""
from typing import List

"""
Amazon OA Problem
"""
class Solution:
    """
    Instead of sorting in the default order, we'll sort in a custom order we specify.

    The rules are:

    Letter-logs come before digit-logs;
    Letter-logs are sorted alphanumerically, by content then identifier;
    Digit-logs remain in the same order.
    It is straightforward to translate these ideas into code.
    """
    def reorderLogFilesBestExample(self, logs: List[str]) -> List[str]:
        # time complexity: O(nlogn) where n is the total content of logs
        # Space complexity: O(n)
        def helper(log):
            identifier, rest = log.split(" ", 1)
            # "let1 art can", so the rest[0] = a = (a)rt
            res = (0, rest, identifier) if rest[0].isalpha() else (1, rest, identifier)  # here is the loop. O(n)
            return res

        return sorted(logs, key=helper)


if __name__ == "__main__":
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    # logs = ["g1 act","a8 act aoo"]
    print(Solution().reorderLogFilesBestExample(logs))
    # ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']
