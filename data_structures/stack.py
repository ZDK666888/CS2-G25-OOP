from doubly_linked_list import DoublyLinkedList

# 2. Stack
class Stack:
    def __init__(self):
        self.dll = DoublyLinkedList()

    def push(self, data):
        self.dll.append(data)  # Push element to the top of stack

    def pop(self):
        if self.is_empty():
            return None
        data = self.dll.tail.data
        self.dll.remove(data)  # Pop element from the top of stack
        return data

    def peek(self):
        return self.dll.tail.data if not self.is_empty() else None # Peek the top element without removal

    def is_empty(self):
        return self.dll.size == 0  # Check if stack is empty

    def size(self):
        return self.dll.size # Return current stack