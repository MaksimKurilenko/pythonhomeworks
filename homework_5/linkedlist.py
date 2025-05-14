class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self._head_node = None
        self._tail_node = None
        self._size = 0

    def append(self, item):
        new_node = Node(item)
        if self._head_node is None:
            self._head_node = self._tail_node = new_node
        else:
            self._tail_node.next = new_node
            new_node.prev = self._tail_node
            self._tail_node = new_node
        self._size += 1

    def prepend(self, item):
        new_node = Node(item)
        if self._head_node is None:
            self._head_node = self._tail_node = new_node
        else:
            new_node.next = self._head_node
            self._head_node.prev = new_node
            self._head_node = new_node
        self._size += 1

    def insert(self, item, i):
        if i <= 0:
            self.prepend(item)
        elif i >= self._size:
            self.append(item)
        else:
            new_node = Node(item)
            current = self._head_node
            for _ in range(i):
                current = current.next
            prev_node = current.prev

            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = current
            current.prev = new_node
            self._size += 1

    def delete(self, item):
        current = self._head_node
        while current:
            if current.data == item:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self._head_node = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self._tail_node = current.prev
                self._size -= 1
                return
            current = current.next
        raise ValueError("Item not found in list")

    def find(self, item):
        current = self._head_node
        while current:
            if current.data == item:
                return current
            current = current.next
        return None

    def display(self, reverse=False):
        elements = []
        if reverse:
            current = self._tail_node
            while current:
                elements.append(current.data)
                current = current.prev
        else:
            current = self._head_node
            while current:
                elements.append(current.data)
                current = current.next
        print("List:", elements)

    def __getitem__(self, i):
        if i < 0 or i >= self._size:
            raise IndexError("Index out of range")
        current = self._head_node
        for _ in range(i):
            current = current.next
        return current.data

    def size(self):
        return self._size

    def __iter__(self):
        return LinkedListIterator(self._head_node)


class LinkedListIterator:
    def __init__(self, node):
        self.current = node

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data
