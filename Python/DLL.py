class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None


class Dlist:
    def __init__(self,value):
        #  point tail to the new node
        node = Node(value)
        self.head = node
        self.tail = node


    def addNode(self,value):
        new_node = Node(value)
        # this new node previous node is the last one
        # whats before the last node you are making the last node
        new_node.prev=self.tail
        # the new next node with the next line is confirmed to be the last node
        self.tail.next = new_node
        self.tail = new_node


    
    def removeNode(self,value):
        # by reference pointer
        # and its even better to have the runner already point to the self.head so you can use it
        # later for the center.
        runner = self.head
        if(runner.value == value):
            # what next to . next
            self.head = runner.next
            # return is just saying its done
            return

        while (runner.next != None):
            # if current value = the inserted value
            if(runner.value == value):
                # this is how you connect the two nodes after you take out the node in between them.
                runner.next.prev = runner.prev
                runner.prev.next = runner.next
                return 
            # this makes ??? the runner the last node???
            runner = runner.next

    def printAllValues(self):
        runner = self.head
        while (runner.next != None):
            print(runner.value)
            runner = runner.next
        print(runner.value)
            # this cant be runner.next otherwise it will print none because there is nothing next its the last one.
            # PLEASE PLEASE DELETE THE COMMENTS BEFORE RUNNING

            # Please also think about the following:

            # How would you know if you have a circular linked list?
            # How would you get to the middle of the linked list?
            # How would you remove duplicate values in the list?
            # How would you reverse the values in the list?
            # Think hard about these puzzles and how you could potentially use multiple runners to tackle some of these tasks.

            # You can spend up to 5 hours on this assignment.




den = Dlist(6)
den.addNode(8)
den.addNode(12)
den.addNode(3)
den.removeNode(6)
den.printAllValues()