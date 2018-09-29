class Queue:
    def __init__(self):
        self.root = []

    def isEmpty(self):
        if self.root != None:
            return True
        else:
            return False
    
    def add(self,data):
        self.root.insert(0,data)
        # self.root.append()

    def remove(self,data):
        self.root.pop()
    
    def printQueue(self):
        for items in self.root:
            print items

    def size(self):
        return len(self.root)
    
    def printQueue(self):
        for items in self.root:
            print items,
            # the comma lets it print all on the same line.

things = Queue()

things.add("a")
things.add("b")
things.add("c")
things.remove("b")
print(things.size())
things.printQueue()
