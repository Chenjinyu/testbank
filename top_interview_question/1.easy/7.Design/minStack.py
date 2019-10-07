"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

"""


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return -1

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return min(self.stack)
        else:
            return -1

# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(1)
minStack.push(2)
print(minStack.stack)
print(minStack.top())
print(minStack.stack)
print(minStack.getMin())
print(minStack.stack)
minStack.pop()
print(minStack.stack)
print(minStack.getMin())
print(minStack.top())
