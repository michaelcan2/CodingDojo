
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

    # def removeNode(self,value):
    #     # self.head is the poonter of where its store adding .value specifcally points to the value of where its 
    #     # stored in memory
    #     if( self.head.value == value):
    #         # what next to . next
    #         self.head = self.head.next
    #         # return is just saying its done
    #         return 
    #     runner = self.head
    #     while (runner.next != None):
    #         # two equal is for comparing 
    #         if (runner.next.value == value):
    #             # then set this = to this , thats wat one equal sign means
    #             runner.next = runner.next.next
    #             return
    #         runner = runner.next

    def zip(self,l1,l2):
        # parameter for linked lists 1 = l1 and linked lists 2 = 2
        # we made l3 an empty b/c we dont know what the value is 
        l3 = ""
        # l1_walker = l1.head 
        # l2_walker = l2.head
        while(l1.next != None or l2.next != None):
            if(l3 == ""):
                # first need to check if l3 is empty.
                # b/ctheir is a value and a next you must specify the value.
                l3 = Slist(l1.value)
                # l3_walker is a current aka walker
                # this goes through l2 list and adds it to l3
                l3.addNode(l2.value)
            else:
                l3.addNode(l1.value)
                l3.addNode(l2.value)
            # if there is a next MAYBE THIS WORKS
            # then the walker will change the next one in the list
            if(l1.next):
                l1 = l1.next
            
            if(l2.next):
                l2 = l2.next
        return(l3)

    def dedupe(self,listP):
        current = self.head
        current2= self.head
        prev = current


        while(current.next != None):
            while(current2.next != None):
                if(current2.next.value == current.value):
                    current2.next = current2.next.next
                # prev = prev.next
                current2 = current2.next
            current = current.next
            current2 = current.next
            # prev = current
        return listP

        # if(current2.next == None)
                    




        
            

list = Slist(6)
list.addNode(8)
list.addNode(9)
list.addNode(2)
list.addNode(6)
list.addNode(28)
list = list.dedupe(list)
list.printAllValues()

# list2 = Slist(16)
# list2.addNode(18)
# list2.addNode(19)
# list2.addNode(12)
# list3 = Slist(0)
# needed to specify like oop to call the zip function within 
# list3 b/c you are inputting 2 different lists
# equal to .zip(whic is two arguments and you want to the return the fusion)
# list3 = list3.zip(list.head, list2.head)
# list3.printAllValues()
# list.removeNode(8)

# list2 = Slist(16)
# list2.addNode(18)
# list2.addNode(19)
# list2.addNode(12)
# list3 = Slist(0)
# list3 = list3.zip(list.head, list2.head)
# list3.printAllValues()

# print(zip([1,3,5], [2,4,6]))


# pointer to access the other functions 


