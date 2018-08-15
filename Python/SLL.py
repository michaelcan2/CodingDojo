
# dennis whats so special about __init__?? its a constructor?? which means??
# below is a constructor for all the nodes
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Slist:
    def __init__(self,value):
        # your creating the node conneting it the node class WHICH HAS THE VALUE
        node = Node(value)
        # your pointing the head to be the new node
        self.head = node


    def addNode(self,value):
        runner = self.head
        # the .next makes it moving till none
        # set the while for what the ending will become
        while runner.next != None:
        # this is the part that makes the runner actually move
            runner = runner.next
        node = Node(value)
        runner.next = node
    
    def printAllValues(self):
        # whatever self.head is putting too I want runner to point to it
        runner = self.head
        while runner.next != None:
        #  prints all the node values while in the loop
            print(runner.value)
        # after printing now in the while loop the runner will be pointing to different nodes in the list
            runner=runner.next
        # this only prints the last one
        print(runner.value)

#     def removeNode(self,value):
#         # self.head is the poonter of where its store adding .value specifcally points to the value of where its 
#         # stored in memory
#         if( self.head.value == value):
#             # what next to . next
#             self.head = self.head.next
#             # return is just saying its done
#             return 
#         runner = self.head
#         while (runner.next != None):
#             # two equal is for comparing 
#             if (runner.next.value == value):
#                 # then set this = to this , thats wat one equal sign means
#                 runner.next = runner.next.next
#                 return
#             runner = runner.next
            

list = Slist(6)
list.addNode(8)
list.addNode(9)
list.addNode(2)
# list.removeNode(8)
list.printAllValues()


# pointer to access the other functions 

# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None

# class Slist:
#     def __init__(self,value):
#         node = Node(value)
#         self.head = node

#     def addNode(self,value):
#         runner = self.head
        
#         while (runner.next != None):
#             runner = runner.next
#         node = Node(value)
#         runner.next = node

#     def printAllValues(self):
#          runner = self.head
#          print(runner.value)
#          while (runner.next != None):
         
#              runner = runner.next
#              print(runner.value)
        

#     def removeNode(self,value):
#         # doesnt this remove the first node?
#         if ( self.head.value == value):
#             self.head = self.head.next
#             print(self.head)
#             return

        # a quesitons
        # def insertNode(self,value):
        # For example, for a linked list with the value of 5 -> 3 -> 1, performing insertNode(7, 2) would insert a Node of value 7 at its 2nd index, making the node 5 -> 3 -> 7 -> 1
        # Please make sure that this method allows you to insert a new node as the first node in the list (if index is 0), anywhere in the middle of the list, or at the end of the list (if the specified index is at the end of the list).

   



        
            
# list = Slist(6)
# list.addNode(8)
# list.addNode(9)
# list.addNode(2)
# list.removeNode(6)
# list.printAllValues()