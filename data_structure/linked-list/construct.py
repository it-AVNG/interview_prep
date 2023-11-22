class Node:
    def __init__(self, value=None):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        """initialize the link list with size and head pointer"""

        self.size = 0
        self.head = None

    def insert(self, value):
        """insert a value to the linked list"""

        if not self.head:
            """if the link list is empty"""
            self.head = Node(value)
        else:
            """if the link list is not empty, add new node to list"""
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def print_list(self):
        """print the current linked list"""
        elements = []
        current = self.head

        while current.next:
            elements.append(current.data)
            current = current.next

        elements.append(current.data)
        return elements

