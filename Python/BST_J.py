
# Trying to fix the REMOVE function 
# it will not do any of the 3 cases i have set up under the if statement num_childern line 194 onward
# WILL PRInt on line 154 it's getting atleast there
class Node:
    def __init__(self,value):
        self.value = value
        self.left_child = None
        self.right_child = None
        # !!!!!!!!!!! this new variable parent will hold a parent of a node when it's place in a tree.
        # this will be set to none for the DELETE function 
        self.parent = None

class binary_search_tree:
    def __init__(self):
        self.root = None
    #--------------------------------- 
    def insert(self,value):
        # in video had two EQUALS
        if self.root == None:
            self.root = Node(value)
        else:
            # if there already is a self.root do this
            # self._insert  <-- is the function CALLING another function
            # value, and self.root is what we are going to be passing into the private
            # function in order to insert into the tree if there is already
            # a root.
            self._insert(value,self.root)
    # ????for the cur_node we are not inputting this somehow this is happening recursively.
    def _insert(self,value,cur_node):
        # recursion example val is 5 value, 7 on left of root node which is 10. root node is 10.
        # 10 the root node is our current value!!!! before recusrion it will always be
        # the first current node
        # **2nd time recursion the cur_node is now 7
        # **2nd time recursion now we ask if 5<7
        if value<cur_node.value:
            # if 7 didnt exist from the root node 10 then 
            # **2nd time recursion check and see if 7 has a left node which it DOES NOT

            if cur_node.left_child == None:
                # then 5 would be the new node of the left side
                # **2ND time recursion now 5 is the left node for 7 yay!! done!!
                cur_node.left_child=Node(value)
                # ^^.leftchild will turn into a node with the value inputed insideit.

                # FOR the DELETE FUNCTION!!!!!!!!!!!!!!!!
                # we now need to alter bst's insert function so that it can correctly set this value after inserting 
                # a new element in the tree.
                cur_node.left_child.parent=cur_node # set parent
            else:
                # since this is using recurion/ contiue the method it doesnt return
                self._insert(value,cur_node.left_child)
                # now we go through the _insert function again, this time we CHANGED the current node 10 to the lower
                # one which is 

            # this above checks if there is at least one node in the tree
            # so then will call the recursive insert function using the root node which is in the node class
            
            
            #Here we do elif instead of just else because, we could have the case where the value is equal to the
            # current node value and we dont want the tree having multiples of the same integers its easier to just pass over 
            # instances like that.
        elif value>cur_node.value:
            # ^^says if value is greater then current node .value
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
                # !!!!!!!!!!!!!!!!! MADE for DELETE FUNCTION
                cur_node.right_child.parent = cur_node # set pare;
                # ..............
                # nt ...was also made for delete
            else:
                self._insert(value,cur_node.right_child)
        # this is the case where the value EQUALS THE CURRENT NODE VALUE AND WILL SIMPLY PRINT "VALUE ALREADU IN TREE!"
        else: 
            print "Value already in tree!"
    #--------------------------------- 


    def print_tree(self):
        # first check if the root is an actual node
        if self.root != None:
            # here we are passing the root as the parameter
            # this is calling
            self._print_tree(self.root) 
            # were gonna be dividing into two functions one reusive and one not like the _insert to make it eaiser to understand
    
    # this private function is gonna pass anode as the only paramter
    def _print_tree(self,cur_node):
        # now we check if the node doesnt equal node
        if cur_node != None:
            # until it hits none it will print
            # ONCE IT HITS NONE IT WILL GO BACK UP TO THE NEXT HIGHEST OF THE RECURISON LIST.
            # print tree passing the left child as the parameter
            self._print_tree(cur_node.left_child)
            # print the value at the current node
            # this is an inorder trasversal of the tree....meaning printed in an inserted order.
            # b/c of the way we put this algos the order will be sorted
            print str(cur_node.value)
            self._print_tree(cur_node.right_child)


    def size(self):
        count = 0
        if self.root != None:
            # you do this recursively so you can go left left left then right 
            # line 106 count returns 115 count
            count = self._size(self.root, count)
            # why print up here not down there
            print count
            return count

    def _size(self, runner, count):
        if runner != None:
            # this +1 is counting the self.root
            count += 1
            # why count = for recursion
            count = self._size(runner.left_child, count)
            count = self._size(runner.right_child, count)
        # why return here??is it to stop
        # when it ends its going to return to line 107
        # and then prints the total of the counts and returns them
        return count




    #--------------------------------- 

    # function that allows us to get a n idea of the actual data structure
    def height(self):
        if self.root != None:
            return self._height(self.root,0)
            # because if our root is equal to none that means are tree obvious has a height of zero. b/c their
            # isnt even an element in the root
        else:
            return 0
            # for private function current node 1st param and an int for the second param 
            # the reason we want to pass an integer is because we want to store the height that we seen on 
            # each recusive call so as were trasvering down the nodes we might be changing this current node
            # but if we didn't have a variable neither as a parameter or stored as say a global variable or an 
            # internal variable inside of the class we wouldnt have a way of knowning the actual height we've 
            #  traversed over the course of all the recursive calls.
            
    def _height(self,cur_node,cur_height):
            # so here the first thing we're checking is if the current node is none were just gonna be returning 
            # the current height because we dont want to increment it at all if the current node were looking 
            # at is obviously doesn't have any value in it.
            if cur_node == None:
                # ^^if cur_node = none then just return height 
                return cur_height
                # next were going to be getting the rest of the height from the left subtree 
                # so starting off from the left child of the current node and doing the same thing
                # on the right subtree so getting the height from the right child on down to the leaves 
                # and then were going to be comparing those seeing which is larger, and then just returning that value
            else:
                left_height=self._height(cur_node.left_child,cur_height+1)
            # = to a recusive call the height^^passing left value as the current node and the current height plus 1 
            # as the current height. because were incrementing the height to allow the value to be tabulated correctly 
            # on the next recursive call and we'll say...
                right_height=self._height(cur_node.right_child,cur_height+1)
                return max(left_height,right_height)
            # ^^^ so this means which ever one is larger the left subtree aka left_height or 
            # right subtree aka right_height is the one that will be returned.
            # ........with this whole function were gonna be doing a comparison at every single node in the tree
            # .......so we will be able to find the part of the tree that has the highest height aka highest level
            # ......the leaves are at. and then once we hit a left the cur_node is gonna be equal to no
            # ....in which case that is gonna be the base case. and will just return the current height.
    
    #-------------------------------------

    # ...FOR DELETE function 
    # add parent in node, add line 38 and line 55
    # this find function returns the node with specified input value 
    # this will return an actual node rather then just a boolean vale like the search function 
    def find(self,value):
        
        # if the value passed in the find function is NOT found in the tree will just return none.
        if self.root != None:
            return self._find(value,self.root)
        else:
            return None

    def _find(self,value,cur_node):
        print(cur_node.value)
        print(value)
    
        if value == cur_node.value:
            print("yo")
            return "True"
        elif value < cur_node.value and cur_node.left_child!=None:
            print("mic check check")
            self._find(value,cur_node.left_child)  
        elif value > cur_node.value and cur_node.right_child != None:
            print("one two one two")
            self._find(value,cur_node.right_child)
        else:
            print("womp womp")
            return "cant find"

    #-------------------------------------

    # ...after we made the find function FOR the delete function we now have all the items we need
    # for the DELETE FUNCTION


    # for a CLEANER user interface we will be declaring two verison of the function 
    # one called delete value, and another called delete node
    # only difference is delete value will be passed an integer, where as delete node will be passed a node
    

    def delete_value(self,value):
        # inside delete value will simply be calling the delete node function, passing the return value of the 
        # find function as the node parameter 
        
        return self.delete_node(self.find(value))
      


    def delete_node(self,Node):
        # inside delete node will first be writing two more HELPER functions the first called MIN_VALUE_NODE
        def min_value_node(n):
            # this will be passed a single node which will be treated as a root of a binary search tree.

            current = n
            # will then traverse down to the left of the tree until it finds the smallest element, returning
            # its value.
            while current.left_child !=None: 
                current = current.left_child
            return current 
        # ^^^^^^will be using this function later to find the next in order successor!!


        # this num_children function will just returns the number of children attached to the inputted node
        def num_children(n):
            print('here!!!!!!')
            num_children=0
            # either 0,1,or 2
            if n.left_child!=None:
                num_children+=1
            if n.right_child!=None:
                num_children+=1
            return num_children

        # will now create variables that hold both the parent of the node to delete as well as the 
        # number of childern.

        # get the parent of the node to be deleted
        node_parent = Node.parent

        # get the number of children of the node to be deleted
        node_children = num_children(Node)

        # break operation into different cases based on the structure of the tree & node to 
        # be deleted

        # the first if statement will cover case 1
        # CASE 1 (node has no children)
        if node_children == 0:

            # setting the appropriate pointer and the parent to none to remove the leaf node.

            # remove reference to the node from the parent 
            if node_parent != None:
                if node_parent.left_child == Node:
                    node_parent.left_child=None
                else:
                    node_parent.right_child=None
            else:
                self.root = None 

        if node_children == 1:
            # this second if statement will cover CASE 2
            # will first create a new variable named child to hold the single child of the node we
            # wish to delete.

            # get the single child node
            if Node.left_child!=None:
            # Here going to maeke a variable named child to hold ths single child of the node
            # we wish to delete.
                child=Node.left_child
            else:
                child=Node.right_child

            if node_parent !=None:
            # will then make the change to the parent node replacing the pointer to the node
            # we wish to delete with the pointer to its child node 

            # replace the node to be deleted with its child
            # this is then making the change to the parent Node replacing the pointer to the Node
            #  we wish to delete with the pointer to its child Node 
                if node_parent.left_child == Node:
                    node_parent.left_child=child
                else:
                # at the end wll update the parent pointer and the child to reflect the fact 
                # we've moved it up a level in the tree.
                    node_parent.right_child=child
            else:
                self.root = child 
            
            # corrects the parent pointer in node
            child.parent=Node.parent 
        

        # CASE 3 (node has two children) where the node we wish to delete has TWO CHILDERN.
        if node_children == 2:
            # IN this case we'll locate the next inorder successor using are mid_value node function
            # will then copy the value we found in that node into the node we wish to delete

            # get the inorder succesor of the deleted node
            successor = min_value_node(Node.right_child)

            # copy the inorder sucessor's value to the node formerly 
            # holding the value we wished to delete
            Node.value = successor.value


            # at the end will call the delete node function recursively this time passing the original
            # inorder successor as the node to delete.
            self.delete_node(successor)
    

    #--------------------------------- 
    
    # now we are implementing a search function vid 25:00
    def search(self,value):
        if self.root != None:
            return self._search(value,self.root)
        else:
            return False

    def _search(self,value,cur_node):
        # if the value equals the value of the current node
        if value == cur_node.value:
            return True
        # value less then the curent node value and the current node does have a left child,
        # ***will be return ing this _search function recursivly and now looking at the left child instead of the
        # current node
        elif value<cur_node.value and cur_node.left_child !=None:
            # cur_node.left_child !=None means that there is no left child ^^
            return self._search(value,cur_node.left_child)
            # ^^ this is the recursion line **will be return ing this _search function recursivly and now 
            # looking at the left child instead of the current node

        elif value>cur_node.value and cur_node.right_child != None:
            return self._search(value,cur_node.right_child)
            # We are returning false if we cant find a match from the value we are searching for
            # false to show that we couldnt find anything in the tree.
            return False

    #--------------------------------- 
    # # no duplicates already implemented in the if statement
    # def NoDupes(self,value):
    #     current = self.root
    #     # current2 = self.head 
    #     while(current != None):
    #         if (current == value):
    #             return False
    #         else:
    #             if(current.value > value):
    #                 current = current.left_child
    #             else:
    #                 current = current.right_child
    #     self.insert(value)
    #     return True 




#------------------------------------
# this function that randomly made numbers to fill the tree
    def fill_tree(tree,num_elems=100,max_int=500):
        from random import randint
        for _ in range(num_elems):
            cur_elem = randint(0, max_int)
            tree.insert(cur_elem)
        return tree



tree = binary_search_tree()
# tree = fill_tree(tree)
tree.insert(5)
tree.insert(4)
tree.insert(6)
tree.insert(10)
tree.insert(9)
tree.insert(11)
tree.size()
tree.find(11)
print (tree.height())
# print(tree.NoDupes(12))
# print(tree.find(11))

# print ("tree height:"+ str(tree.height()))

# tree.delete_value(10)
# tree.print_tree()
# tree.size()            

# the order on how it prints is inorder transversal