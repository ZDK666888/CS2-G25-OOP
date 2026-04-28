from doubly_linked_list import DoublyLinkedList

# 3. Queue
class Queue:
    def __init__(self):
        self.dll = DoublyLinkedList()

    def enqueue(self, data):
        self.dll.append(data)  # Enqueue element at the rear

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.dll.head.data
        self.dll.remove(data)  # Dequeue element from the front
        return data

    def peek(self):
        return self.dll.head.data if not self.is_empty() else None # Peek front element without removal

    def is_empty(self):
        return self.dll.size == 0  # Check if queue is empty

    def size(self):
        return self.dll.size # Return current queue