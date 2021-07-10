# Advanced Stack Problem:
# To design a stack such that getMinimumElement should always be O(1)

class Stack:
    def __init__(self, data=None):
        self.capacity = 10
        self.top = -1
        self.arr = [None] * self.capacity
        if data is not None:
            for data in data:
                self.push(data)

    def push(self, data):
        if self.top + 1 == self.capacity:
            print("Stack overflow !!!")
            return
        self.top = self.top + 1
        self.arr[self.top] = data

    def pop(self):
        if self.top == -1:
            print("Stack Underflow !!!")
            return
        temp = self.arr[self.top]
        self.top = self.top - 1
        return temp

    def peek(self):
        if self.top == -1:
            print("Stack Underflow !!")
            return
        return self.arr[self.top]

    def is_empty(self):
        return self.top == -1

    def top_position(self):
        return self.top


class AdvancedStack:
    def __init__(self, elementStack, minStack):
        if elementStack is None or minStack is None:
            print("Stacks not initialised.")
            return False
        self.elementStack = elementStack
        self.minStack = minStack

    def push(self, data):
        if data is None:
            print("Invalid data !!")
            return
        self.elementStack.push(data)
        if self.minStack.is_empty() or self.minStack.peek() > data:
            self.minStack.push(data)
        else:
            self.minStack.push(self.minStack.peek())

    def pop(self):
        if self.elementStack.is_empty():
            print("Stack underflow !!!")
            return False
        temp = self.elementStack.pop()
        self.minStack.pop()
        return temp

    def get_minimun(self):
        if self.minStack.is_empty():
            print("Stack Underflow !!!")
            return
        return self.minStack.peek()


elementStack = Stack()
minStack = Stack()
advStack = AdvancedStack(elementStack, minStack)
advStack.push(10)
advStack.push(12)
advStack.push(2)
print("Min Element Checkpoint #1 ->", advStack.get_minimun())
advStack.pop()
advStack.push(100)
advStack.push(8)
print("Min Element Checkpoint #2 ->", advStack.get_minimun())
