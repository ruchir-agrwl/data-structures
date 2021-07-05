# Linked List bases implementation of Stack

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def has_next(self):
        return self.next != None


class Stack:
    def __init__(self, data=None):
        self.head = None
        if data is not None:
            for data in data:
                self.push(data)

    def push(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def pop(self):
        if self.head is None:
            raise IndexError
        temp = self.head
        self.head = self.head.next
        return temp.data

    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.data


l = [1, 2, 3, 4, 5]
stack = Stack(l)
print("Pop ->", stack.pop())
print("Peek ->", stack.peek())
stack.push(6)
print("Pop ->", stack.pop())
