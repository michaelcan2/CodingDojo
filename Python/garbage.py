class Node:
    def __init__(self,value):
        self.value= value
        self.next = None


class Sll:
    def __init__(self,value):
        node = Node(value)
        self.head = node

    def addNode(self,value):
        current =  self.head 
        while(current.next != None):
            current = current.next
        node = Node(value)
        # need 
        current.next = node

    def printAll(self):
        current = self.head
        while(current.next != None):
             print current.value 
             current = current.next
        print current.value 

    def length(self):
        runner = self.head
        count = 0
        while(runner != None):
            count += 1
            runner = runner.next 
        print count 


# PROBLEM MOVE MAX TO BACK
    def Max(self):
        highest = 0
        runner = self.head
        while(runner != None):
            if runner.value > highest:
                highest = runner.value
                runner = runner.next
        # move = <--maybe need another pointer.
        while(highest = runner.value):
            # how do i make the highest node move to
            # the end of the linked list by not reassign
            # highest node accidentally
            


# need help finding smallest
    def lowest(self):
        lowest = 1
        runner = self.head
        # making it runner instead of runner.next
        # includes the number.
        while(runner != None):
            if runner.value =< lowest:
                lowest = runner.value
                runner = runner.next
        print lowest
# what exactly is the average that I am looking for in the sll

        



# sort linked list by making the biggest number 
# start from biggest to smallest
# also find min

list = Sll(1)
# list.addNode(2)
list.addNode(9)
list.addNode(15)
# list.printAll()
# list.length()
# list.Max()
list.lowest()
              



        


