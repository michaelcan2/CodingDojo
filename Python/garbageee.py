class Stack:
    def __init__(self):
        self.root = []

    def push(self,data):
        return self.root.append(data)

    def pop(self):
        return self.root.pop()

    def get(self):
        return self.root

    def empty(self):
        if self.root == []:
            return True
        else:
            return False

    def peek(self):
        if self.root != None:
            return self.root[-1]

thing = Stack()


thing.push(1)
thing.push(2)
thing.push(3)


print thing.peek()




