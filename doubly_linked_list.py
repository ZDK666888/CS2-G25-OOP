# 0. Doubly Linked List Node
# Shared by doubly linked list, stack and queue
class Node:
    def __init__(self, data):
        self.data = data    # stored data
        self.prev = None    # previous node pointer
        self.next = None    # next node pointer

# 1. Doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Add node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    # Add node at the beginning of the list
    def prepend(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    # Remove node by given data value
    def remove(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next # Handle head node
                if current == self.tail:
                    self.tail = current.prev # Handle tail node

                if current.prev:
                    current.prev.next = current.next # Link previous node to next node
                if current.next:
                    current.next.prev = current.prev # Link next node to previous node
                self.size -= 1
                return
            current = current.next

    # Forward traversal and return formatted string
    def traverse_forward(self):
        res = []
        current = self.head
        while current:
            res.append(str(current.data))
            current = current.next
        return " <-> ".join(res)