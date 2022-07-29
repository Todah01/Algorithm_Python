class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return "Empty"

        del_node = self.head

        if self.nead.next is None:
            self.head = None
            self.tail = None
            return del_node.data

        self.head = self.nead.next
        return del_node.data

    def peek(self):
        if self.is_empty():
            return "Empty"
        return self.head.data

    def is_empty(self):
        return self.head is None
