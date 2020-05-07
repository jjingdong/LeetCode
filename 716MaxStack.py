'''
716. Max Stack
Easy

Design a max stack that supports push, pop, top, peekMax and popMax.

	1.	push(x) -- Push element x onto stack.
	2.	pop() -- Remove the element on top of the stack and return it.
	3.	top() -- Get the element on the top.
	4.	peekMax() -- Retrieve the maximum element in the stack.
	5.	popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.

Example 1: 
MaxStack stack = new MaxStack();
stack.push(5);
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5

Note: 
	1.	-1e7 <= x <= 1e7
	2.	Number of operations won't exceed 10000.
	3.	The last four operations won't be called when stack is empty.
'''


class MaxStack:

    # Using 2 stacks
    # 5. 5
    # 1  5
    # 5  5
    # Note. list.pop() return the value just pop-ed
    #
    # Note. It's hard to debug, just leave it for now

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

        if self.maxStack == []:
            self.maxStack.append(x)
        else:
            top = self.maxStack[-1]
            if top > x:
                self.maxStack.append(top)
            else:
                self.maxStack.append(x)

    def pop(self) -> int:

        if self.stack == []:
            return None
        else:
            self.maxStack.pop()
            temp = self.stack[-1]
            self.stack.pop()
            return temp

    def top(self) -> int:
        if self.stack == []:
            return None
        else:
            return self.stack[-1]

    def peekMax(self) -> int:
        if self.maxStack == []:
            return None
        else:
            return self.maxStack[-1]

    def popMax(self) -> int:
        if self.stack == None:
            return None
        else:
            max = self.maxStack[-1]
            temps = []
            temp = 0
            while self.stack[-1] != max:
                temp = self.stack[-1]
                self.stack.pop()
                self.maxStack.pop()
                temps.append(temp)

            for i in range(len(temps)):
                self.stack.push(temps[-1 + i])
                self.maxstack.push(temps[-1 + i])

            return max

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()