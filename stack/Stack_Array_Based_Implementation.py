# Simple Array bases implementation of Stack
class Stack:
    def __init__(self, capacity=None):
        self.top = -1
        self.capacity = capacity
        self.A = [None] * capacity

    def push(self, data):
        if self.top + 1 == self.capacity:
            print("Stack Overflow !!")
            return
        self.top = self.top + 1
        self.A[self.top] = data

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return
        temp = self.A[self.top]
        self.top = self.top - 1
        return temp

    def peek(self):
        if self.top == -1:
            print("Stack Underflow !")
            return
        return self.A[self.top]

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top + 1 == self.capacity


stack = Stack(10)
for i in range(10):
    stack.push(i)

print("Peeking stack ->", stack.peek())
print("Is stack empty ->", stack.isEmpty())
print("Is stack Full ->", stack.isFull())
for x in range(12):
    temp = stack.pop()
    if temp is not None:
        print("Pop ->", temp)
