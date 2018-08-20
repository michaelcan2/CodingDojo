class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SLL:
    def __init__(self,value):
        node= Node(value)
        self.head = node

    # all stuff on regular linked list