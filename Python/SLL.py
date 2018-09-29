# IF ITS STILL RUNNING YOUR STUCK IN A LOOP

import math
# dennis whats so special about __init__?? its a constructor?? which means??
# below is a constructor for all the nodes
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        # this makes sense b/c the last node will be set to none.

# class Slists is a wrapper of the Node
class Slist:
    def __init__(self,value):
        # You will be making more then one node here the properties of the node
        # will be needed to give self.head the same propties
        # since self.head will = node it will be owning/covering that node
        # which means you will have to reexplain how what a node is 
        # and let it be free.
        node = Node(value)
        # this is simply YOUR POINTER TO the first node
        # self.head is NOT the pointer itself
        # for alot of function you will need to start at the head
        # thanks to self.head you will be able to easily point to 
        # the front AKA head of the SLL.
        self.head = node

    def length(self):
        count = 0
        while(self.head != None):
            count += 1
            self.head = self.head.next
        print count 
        
    def Max(self):
        highest = 0
        runner = self.head
        while(runner != None):
            if runner.value > highest:
                highest = runner.value
            # you were only incrementing the runner when it's value was greater then
            # the highest value//// when it was indented to the right
            runner = runner.next
        print highest

    def Min(self):
        # any integer is less then a string 
        # if you compare any number to a string its gonna be less,
        # w/e the first self.head is will be the first value.
        # here we dont know what the lowest value is so we 
        lois = ""

        runner = self.head
        # lois = runner.value  <--if you do it this way you dont need line 49
        while(runner != None):
            if runner.value < lois:
                lois = runner.value
            # you were only incrementing the runner when it's value was greater then
            # the highest value//// when it was indented to the right
            runner = runner.next
        print lois

    def append(self,value,after):
        runner = self.head
        while runner != None:
            if runner.value == after:
                # after.next.next  will need to point to something else to
                # not get over written
                temp = runner.next
                node = Node(value)
                runner.next = node
                # runner.next = self.addNode(value)
                # print runner.value
                runner.next.next = temp
                return
            runner = runner.next
        # this line is if it didnt find the value then it will break out of the while
        # loop and add it at the end.
        # node = Node(value)
        # runner.next = node

        # this line has it input into the sll at the end even if there is no after number which you inputted
        self.addNode(value)
        # runner.next = self.addNode(value)
        return





    def avg(self):
        total =0
        count = 0
        runner = self.head
        while(runner != None):
            total += runner.value
            count += 1
            runner = runner.next
        return total/ count

    def addNode(self,value):
        runner = self.head
        # you make runner now the pointer that is self.head you
        # transferring the power of the pointer to something eaiser to 
        # type.
        # the .next makes it moving till none
        # set the while for what the ending will become
        while runner.next != None:
        # this is the part that makes the runner actually move
            runner = runner.next
        node = Node(value)
        # needed extra one after loop because your adding one
        runner.next = node
    
    def printAllValues(self):
        # whatever self.head is putting too I want runner to point to it
        runner = self.head
        value = ""
        while runner != None:
        #  prints all the node values while in the loop
        # this prints every num in its own line
            # print(runner.value)
            # adding all of them into a string
            value = value + str(runner.value)

        # after printing now in the while loop the runner will be pointing to different nodes in the list
            runner=runner.next
        # this only prints the last one
        # this prints every num in its own line
        # print(runner.value)
        print value

    def removeNode(self,value):
        # self.head is the poonter of where its store adding .value specifcally points to the value of where its 
        # stored in memory
        if( self.head.value == value):
            # what next to . next
            self.head = self.head.next
            # return is just saying its done
            return 
        runner = self.head
        while (runner.next != None):
            # two equal is for comparing 
            if (runner.next.value == value):
                # then set this = to this , thats wat one equal sign means
                runner.next = runner.next.next
                return
            runner = runner.next

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
            while(current.next != None):
                while(current2.next != None):
                    if(current2.next.value == current.value):
                        current2.next = current2.next.next
                    if(current2.next != None):
                        current2 = current2.next
                if(current.next != None):
                    current = current.next
                    current2 = current
            return listP









# !!!!!!! ALLLL WRONG
    # def dedupe(self,listP):
    #     current = self.head
    #     current2= self.head
    #     prev = current


    #     while(current.next != None):
    #         while(current2.next != None):
    #             if(current2.next.value == current.value):
    #                 current2.next = current2.next.next
                # prev = prev.next
            #     current2 = current2.next
            # current = current.next
            # current2 = current.next
            # prev = current
        # return listP

        # if(current2.next == None)
                    




        
        #    always wrap the variable from left to right
        # left conquers over right

list = Slist(6)
list.addNode(8)
list.addNode(9)
list.addNode(2)
list.addNode(15)
# list.Max()
# list.Min()
list.append(3,8)
list.append(18,28)
# list.addNode()
# list.removeNode(8)
# list = list.dedupe(list)
# DE
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


