class Node:
    def __init__(self, data):
        self.data = data
        self.both = 0

class MemoryEfficientDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.both = id(self.head)
            self.head.both ^= id(new_node)
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.both = id(self.tail)
            self.tail.both ^= id(new_node)
            self.tail = new_node

    def print_list(self):
        current = self.head
        prev = 0
        while current:
            print(current.data, end=" ")
            next_node = current.both ^ prev
            prev = id(current)
            current = next_node if next_node == 0 else get_node(next_node)
        print()

def get_node(addr):
    return ctypes.cast(addr, ctypes.py_object).value

import ctypes
# Example usage
medll = MemoryEfficientDoublyLinkedList()
medll.insert_at_end(1)
medll.insert_at_end(2)
medll.insert_at_end(3)
medll.print_list()  # Output: 1 2 3