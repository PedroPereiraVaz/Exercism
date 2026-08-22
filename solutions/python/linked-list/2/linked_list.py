class Node:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.prev = previous

    


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    # def __iter__(self):
    #     pass
    
    def info(self):
        print("INFO::::::")
        if self.head:
            print("HEAD ",self.head.value)
        else:
            print("NO HAY HEAD")
        if self.tail:
            print("TAIL ",self.tail.value)
        else:
            print("NO HAY TAIL")
        print(".................")

    def add_first_node(self, node):
        self.head = node
        self.tail = node

    def del_last_node(self):
        self.head = None
        self.tail = None

    def push(self, value):
        if not self.tail:
            self.add_first_node(Node(value))
        else:
            new_node = Node(value, previous=self.tail)
            self.tail.next = new_node
            self.tail = new_node
            
        self.size +=1

    def unshift(self, value):
        if not self.head:
            self.add_first_node(Node(value))
        else:
            new_node = Node(value, next= self.head)
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def pop(self):
        if not self.tail:
            raise IndexError("List is empty")

        pop_node = self.tail

        if self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.del_last_node()
        self.size -= 1
        return pop_node.value

    def shift(self):
        if not self.head:
            raise IndexError("List is empty")

        shift_node = self.head

        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.del_last_node()
        
        self.size -= 1
        return shift_node.value

    def delete(self, value):
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
                    next_node = actual_node.next
                    
                    prev_node.next = next_node
                    next_node.prev = prev_node

                    self.size -= 1    
                return

            actual_node = actual_node.next
        raise ValueError("Value not found")