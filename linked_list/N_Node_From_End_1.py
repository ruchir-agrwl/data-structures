# Program to find n Node from end
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
        temp = self.head
        while temp is not None:
            if temp.next is None:
                temp.next = Node(data)
                break
            temp = temp.next

    def find_n_from_end(self, n):
        m = -1
        temp = self.head
        while temp is not None:
            m = m + 1
            temp = temp.next
        if n > m:
            print("Required position is greater than the length of the Linked List !")
            return None
        pos = 0
        temp = self.head
        while temp is not None:
            if pos == m - n + 1:
                print("{0} element from end is ->{1}".format(n, temp.data))
                return temp.data
            temp = temp.next
            pos = pos + 1
        return None


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
l.find_n_from_end(10)
