class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self._first_node = None
        self._last_node = None
        self._size = 0

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self._first_node = self._last_node = new_node
        else:
            self._last_node.next = new_node
            self._last_node = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        item = self._first_node.data
        self._first_node = self._first_node.next
        if self._first_node is None:
            self._last_node = None
        self._size -= 1
        return item

    def front(self):
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self._first_node.data

    def is_empty(self):
        return self._first_node is None

    def size(self):
        return self._size

    def display(self):
        current = self._first_node
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Queue (front -> back):", elements)

    def __iter__(self):
        return QueueIterator(self._first_node)


class QueueIterator:
    def __init__(self, start_node):
        self.current = start_node

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data
