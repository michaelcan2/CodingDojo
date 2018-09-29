


# this would also work without a leaf class. It would also work to put None at the 
# leaves but then we'd have to check for it rather than simply calling a method on it. 



# -------------------------------
class twoNode:
    def __init__(self,data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def count(self):
        count = 0
        # made this variable b/c you have to keep track of it.
        if self.left != None:

            count += self.left.count() 
            # this adds to the count variable w/e count we find in this reursion fxn.


        elif self.right != None:
            count += self.right.count()
            
        return 1 + count
        # took outthe parenthesis b/c its a variable not a function.

        
# IS THIS THE CORRECT WAY TO USE NONE AND NOT HAVE LEAD CLASS 
    def search(self,data):
        if  data == None:
            return None

        # do i need THIS CHEK OR IS THE ONE AFTER IT THE SAME THING
        else:
            # ^^dont need data !=None but youll have it there.
            if data == self.data:
                return True

            elif data > self.data and self.right != None:
                return self.right.search(data)

            elif data < self.data and self.left != None:
                return self.left.search(data)

class ThreeNode:
    def __init__(self,data1,data2,left=None,right=None,middle=None):
        self.data1 = data1
        self.data2 = data2
        self.left = left
        self.right = right 
        self.middle = middle

    def count(self):
        count = 0

        if self.left != None:
            count += self.left.count()
        elif self.right != None:
            count += self.right.count()
        elif self.middle != None:
            count += self.middle.count()

        return 2 + count

    def search(self,data):
        print('surprise')
        if self.data1 == None and self.data2 == None:
            return False

        elif data == self.data1 or data == self.data2:
            return True
        elif data < self.data1 and self.left != None:
            # CANT HAVE DATA > SELF.DATA1 B/C IT WILL ALSO BE GREATER THEN DATA TWO SO IT WILL TRUE FOR THE MIDDLE AND THE RIGHT.
            # would I need another elif to check if self.right is not None
            # before i continue???
            # elif self.right == None
            # NOT SURE WHAT TO DO NEXT IF THIS IS THE CASE.
            return self.left.search(data)
            # put^^data in the search otherwise it wont know what its searching for.

        elif data < self.data2 and self.middle != None:
            return self.middle.search(data)
        elif data > self.data2 and self.right != None:
            return self.right.search(data)

class TwoThreeTree:
    def __init__(self,root=None):
        self.root=root

    def count(self):
        # when would it know to return this fxn
        return self.root.count(
        )
    def search(self,data):
        return self.root.search(data)

print TwoThreeTree(ThreeNode(8,10,twoNode(2))).search(9)

# !!!!!oN THREE NODECHECK TIME COMPLEXITIES 


# class TwoThreeTree:
#     def __init__(self,root=LEAF):
#         self.root = root

#     def count(self):
#         return self.root.count()
#     def search(self,data):
#         return self.root.search()




# class leaf:
#     def __init__(self):
#         pass

#     def count(self):
#         return 0

#     def search(self,data):
#         return False

# class TwoNode:
#     def __init__(self,data,left=LEAF,right=LEAF):
#         self.data = data
#         self.left = left
#         self.right = right

#     def count(self):
#         return 1 + self.left.count() + self.right.count()

#     def search(self,data):
#         if data == self.data:
#             return True
#         elif data > self.data:
#             return self.right.search()
#         else:
#             return self.left.search()
#             # 1!!!! why not have one return flase or an else for false?

# class ThreeNode:
#     def __init__(self,data1, data2, left=LEAF,right=LEAF,middle=LEAF):
#         self.data1 = data1
#         self.data2 = data2
#         self.left = left
#         self.right = right
#         self.middle = middle

#     def count(self):
#         return 2 + self.left.count() + self.right.count() + self.middle.count()

#     def search(self,data):
#         if data == self.data:
#             return True
#         elif data < self.left:
#             return self.left.search()
#         elif data < self.middle:
#             return self.middle.search()
#         else:
#             return self.right.search()




    # def printAll(self):
    #     if self.root != None:
    #         self._printAll(self,self.root)

    # def _printAll(self,cur_node):
    #     if cur_node != None:
    #         self._printAll(cur_node.left_child)
    #         # what happens when it doesnt print as a str.
    #         print(cur_node.value)
    #         self._printAll(cur_node.right_child)

    # def size(self):
    #     if self.root != None:
    #         count = self._size(self,self.root,count)
    #         print count 
    #         return count 

    # def _size(self,cur_node):
    #     if runner != None:
    #         count += 1
    #         # why do I need to = count to below?and not have it just play
    #         # by itself
    #         count = self.count(cur_node.left_child)
    #         count = self.count (cur_node.right_child)
    #     return count


    #     if cur_node != None:
    #         self._size(cur_node.left_child)
    #         count +=1
    #         self._size(cur_node.right_child)
        



        









