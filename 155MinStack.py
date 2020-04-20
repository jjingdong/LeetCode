# 155. Min Stack
# Easy
#
# Share
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# 	•	push(x) -- Push element x onto stack.
# 	•	pop() -- Removes the element on top of the stack.
# 	•	top() -- Get the top element.
# 	•	getMin() -- Retrieve the minimum element in the stack.
#  
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

class MinStack:

    # Time O(1)
    # Space O(N)
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stack_min = []

    def push(self, x: int) -> None:

        if self.stack == []:
            self.stack_min.append(x)
        else:
            if self.stack_min[-1] > x:
                self.stack_min.append(x)
            else:
                self.stack_min.append(self.stack_min[-1])

        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()
        self.stack_min.pop()

    def top(self) -> int:
        if self.stack == []:
            return None
        else:
            return self.stack[-1]

    def getMin(self) -> int:

        if self.stack == []:
            return None
        else:
            return self.stack_min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()