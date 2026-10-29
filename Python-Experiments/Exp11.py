# Experiment 11: Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_beginning(self):
        if self.head:
            self.head = self.head.next
        else:
            print("List is empty")

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Creating and using the linked list
ll = LinkedList()
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_end(40)

print("Linked list:")
ll.display()

ll.delete_beginning()
print("After deleting first node:")
ll.display()

# Doubly linked list node
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

first = DNode(10)
second = DNode(20)
first.next = second
second.prev = first

print("Doubly linked list:", first.data, "<->", first.next.data)
