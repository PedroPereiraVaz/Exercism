"""Module for linked list"""
class Node:
    """Node"""
    def __init__(self, value, next_node=None, previous=None):
        self.value = value
        self.next_node = next_node
        self.prev = previous

    def __repr__(self):
        """Print"""
        return f"Node({self.value})"


class LinkedList:
    """ Linked List """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        """Size"""
        return self.size

    def __iter__(self):
        """Iter"""
        actual_node = self.head
        while actual_node:
            yield actual_node.value
            actual_node = actual_node.next_node
    
    def add_first_node(self, node):
        """Add first node"""
        self.head = node
        self.tail = node

    def del_last_node(self):
        """Delete last node"""
        self.head = None
        self.tail = None

    def push(self, value):
        """Add node to end list"""
        if not self.tail:
            self.add_first_node(Node(value))
        else:
            new_node = Node(value, previous=self.tail)
            self.tail.next_node = new_node
            self.tail = new_node
            
        self.size +=1

    def unshift(self, value):
        """Add node to start list"""
        if not self.head:
            self.add_first_node(Node(value))
        else:
            new_node = Node(value, next_node= self.head)
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def pop(self):
        """Delete last node and return"""
        if not self.tail:
            raise IndexError("List is empty")

        pop_node = self.tail

        if self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next_node = None
        else:
            self.del_last_node()
        self.size -= 1
        return pop_node.value

    def shift(self):
        """Delete frist node and return"""
        if not self.head:
            raise IndexError("List is empty")

        shift_node = self.head

        if self.head.next_node:
            self.head = self.head.next_node
            self.head.prev = None
        else:
            self.del_last_node()
        
        self.size -= 1
        return shift_node.value

    def delete(self, value):
        """Delete any node in list"""
        if self.size == 0:
            raise ValueError("Value not found")
        actual_node = self.head

        while actual_node:
            if actual_node.value == value:
                if actual_node == self.head:
                    self.shift()
                elif actual_node == self.tail:
                    self.pop()
                else:
                    prev_node = actual_node.prev
                    next_node = actual_node.next_node
                    
                    prev_node.next_node = next_node
                    next_node.prev = prev_node

                    self.size -= 1    
                return

            actual_node = actual_node.next_node
        raise ValueError("Value not found")

