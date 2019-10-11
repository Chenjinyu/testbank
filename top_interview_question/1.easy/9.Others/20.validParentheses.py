"""
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

NOTE:
the better solution is using stack. push and pop in only one stack.
"""

class Solution:
    # Time: O(n2), Space: O(n).
    # coz the every time the s = s.replace() will create a new s.
    def isValidIDID(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        parentheses_list = ['[]', '{}', '()', '<>']
        i, length = 0, len(s) // 2
        while i <= length:
            for p in parentheses_list:  # here occupied a lot of time space.
                if s.find(p) >= 0:
                    s = s.replace(p, '')   # and here occupied a lot of memory for each s.
            i += 1

        if s == "":
            return True
        else:
            return False
            
    def isValidEfficient(self, s: str) -> bool:
        stack = []
        for c in s:
            # the if else can be improved as the isValidEfficientMore funciton
            # using the dict{key: val}
            if c in "([{":
                stack.append(c)
            elif c == ")":
                if len(stack) == 0 or stack.pop(-1) != "(":  # pop(-1) is the first one push into.
                    return False
            elif c == "]":
                if len(stack) == 0 or stack.pop(-1) != "[":
                    return False
            else:  # if c == "}":
                if len(stack) == 0 or stack.pop(-1) != "{":
                    return False
        return False if len(stack) > 0 else True


    def isValidEfficientMore(self, s: str) -> bool:
        # very good solution. 
        mapping = {')': '(', '}': '{', ']': '['}
        if not s: return True
        stack = []
        for char in s:
            if char in mapping.keys():
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
        
        
if __name__ == "__main__":
    s = "{{{[()]}}}"
    # s = "{[[]()]}"
    # s = "[{(})]"
    print(Solution().isValidEfficientMore(s))
            
