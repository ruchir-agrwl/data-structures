class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def add_at_end(self, data):
        temp = Node(data)
        current = self.head
        if current is None:
            self.head = temp
        while current is not None:
            if current.next is None:
                current.next = temp
                break
            current = current.next

    def delete(self, data):
        current = self.head
        if current is None:
            print("Empty Linked List, Delete operation unsuccessful !")
            return
        if current.data == data:
            self.head = current.next
            print("Element Deleted Successfully !")
            return
        temp = current
        current = current.next
        while current is not None:
            if current.data == data:
                temp.next = current.next
                print("Element {0} deleted successfully !".format(data))
                return
            temp = temp.next
            current = current.next

    def search(self, data):
        if self.head is None:
            print("List is empty, element not found !")
        current = self.head
        pos = 1
        while current is not None:
            if current.data == data:
                print("Element found at {0} position".format(pos))
                return
            pos = pos + 1
            current = current.next
        print("Element {0} not found in Linked List !!".format(data))

    def traverse_list(self):
        if self.head is None:
            print("List is Empty !!")
            return
        print("Traversing the Linked List ->")
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


my_list = LinkedList()
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.traverse_list()

my_list_1 = LinkedList()
my_list_1.add_at_end(1)
my_list_1.add_at_end(2)
my_list_1.add_at_end(3)
my_list_1.traverse_list()
my_list_1.search(2)
my_list_1.search(20)
my_list_1.delete(23)
my_list_1.delete(3)
my_list_1.traverse_list()
