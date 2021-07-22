# Program to detect a loop in Linked List.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def traverse(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
        return

    def get_head(self):
        return self.head

    def detect_cycle(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while slow_ptr and fast_ptr:
            fast_ptr = fast_ptr.next
            if fast_ptr == slow_ptr:
                return True
            if fast_ptr == None:
                return False
            fast_ptr = fast_ptr.next
            if fast_ptr == slow_ptr:
                return True
            slow_ptr = slow_ptr.next


l = LinkedList()
l.add(10)
l.add(20)
l.add(30)
l.add(40)
l.add(50)
l.add(60)
l.add(70)
l.add(80)
l.add(90)
l.add(100)
l.traverse()
