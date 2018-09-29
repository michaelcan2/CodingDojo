class Node:
    def __init__(self,value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent=None

class Bst:

    def __init__(self):
        self.root = None
    # you have self here b/c its gonna use itself
    def insert(self,value):
        if self.root == None:
            self.root = Node(value)
        else:
            # recursion always need self? to call on itself
            # here your comparing the value with the root of the bst
            self._insert(value,self.root)
    # !!!!!!!!!!DENNISS is the true!!!
    # this needs self as well b/c its calling on itself?
    # right now because of recursion cur_node is simply a pointer for 
    # self .root
    def _insert(self,value,cur_node):
        if(value > cur_node.value):
            if(cur_node.right_child == None)
            cur_node.right_child = Node(value)
        else:
            self._insert(value,cur_node.right_child)


        elif(value < cur_node.value):
            if(cur_node.left_child == None):
                # !!!!!!!!!!!!!!!
                # this node is made with the value we 
                # have inputted into the tree right!!!!
                cur_node.left_child = Node(value)

            else:
                self._insert(value,cur_node.left_child)
        
        else:
            print "already value in the tree"

    def printAll(self):
        if self.root != None:
            # this makes us start with self.root
            self._printAll(self.root)
# how do you go both left and right
# it has to be two TRUE if statements
# to go left and right
    def _printAll(self,cur_node):
        # but now we have a pointer that could be none
        if cur_node != None:
            print cur_node 





class Node:
    def __init__(self,value)
    self.value = None
    self.right_child = None
    self.left_child = None
    self.parent = None

# when you do self the name of your bst dot value/right_child etc..
# will be used to print your answer

class Bst:
    def __init__(self):
        self.root = None
        # every bst will have a self.root = to none.
        # ???????????
        # But why cant we have a value in the constructor just for the self.root
        # instead of putting it in the insert fxn???

    def insert(self,value):
        if self.root == None:
            self.root = Node(value)
        else:
            # self is calling that..which is why we need it.
            self._insert(self,value,cur_node)

    def _insert(value,cur_node):
        if value > cur_node:
            if cur_node.right_child.value == None:
                value = cur_node.right_child.value
            else:
            self._insert(value,cur_node.right_child)
        
        if value < cur_node:
            if cur_node.left_child.value == None:
                value = cur_node.left_child.value
            else:
            self._insert(value,cur_node.left_child)
            


                # what now if the cur_node.left_child.value ISNT NONE

    def printAll(self):
        if self.root != None:
            self._printAll(self.root)
            # cause were going to be starting at the begining

    def _printAll(self,cur_node):
        if cur_node != None:

# go over on paper how size printa
# THIS DOESNT HAVE ANY GLOBAL VARIABLES CORRECT??


    def size(self):
        count = 0
        if(self.root != None):
            self._size(self.root,count)
            print count 

    def _size(self, cur_node_RUNNER,count):
        if runner != None:
            count += 1
            self._size(runner.left_child,count)
            self._size(runner.right_child,count)

    def find(self,value):
        if self.root != None:
            return self._find(value,self.root)
        else:
            print "tree empty"

    def _find(self,value,cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child != None:
            self._find(value,cur_node.left_child)
        else value > cur_node.value and cur_node.right_child != None:
            self._find(value,cur_node.right_child)


    def printAll(self):
        if self.root != None:
            self._print(self.root)

    def _printAll(self,cur_node):
        if cur_node != None:
            self._printAll(cur_node.left_child)

            print str(cur_node.value)

            self._printAll(cur_node.right_child)

    def print_all(self,cur_node):
        if cur_node != None:
            self._printAll(cur_node.left_child)

            print str(cur_node.value)

            self._printAll(cur_node.right_child)











        







    # write a fxn that makes a test case if there is nothing to print for left.child 
    # 
class Node:
    def __init__(self,value):
        self.value = value
        self.left_child = None
        self.right_child = None


class Bst:
    def __init__(self,value):
        self.root = None

    def add(self,value):
        if self.root == None:
            self.root = value
        else: 
            self._add(value,self.root)

    def _add(value,cur_node):
        if value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
            else:
                self._add(value,cur_node.right_child)

        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
            else:
                self._add(value,cur_node.left_child)
            











    
    def add(self,value):
        if self.root != None:
            self._add(value,self.root)
        else:
            self.root = Node(value)


    def _add(value, cur_node):
        if value < cur_node.value:
            
            if cur_node.left_child == None:
                 cur_node.left_child = Node(value)

        elif value > cur_node.value:
            if cur_node.right_child == None:
            cur_node.right_child = Node(value)

        else:
            "already in the tree"


    

    def print(self):


given_array = [1,2,3,4,5,6,7,8,9,10]

    def sum(arr):
        total = 0
        for i in arr:
            total += i
            print total

sum(given_array)


class Node: 
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2
        self.left_child = None
        self.middle_child = None
        self.right_child = None 

    def 

