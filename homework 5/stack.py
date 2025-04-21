class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 


class Stack:
    def __init__(self):
        self._top_node = None  
        self._size = 0         

    def push(self, item):
        new_node = Node(item)
        new_node.next = self._top_node 
        self._top_node = new_node       
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        item = self._top_node.data
        self._top_node = self._top_node.next  
        self._size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._top_node.data

    def is_empty(self):
        return self._top_node is None

    def size(self):
        return self._size

    def display(self):
        current = self._top_node
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Stack (top -> bottom):", elements)

    def __iter__(self):
        return StackIterator(self._top_node)


class StackIterator:
    def __init__(self, start_node):
        self.current = start_node

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data
