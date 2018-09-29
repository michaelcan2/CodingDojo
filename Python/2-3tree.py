class leaf:
    def __init__(self):
        pass

    def count(self):
        return 0

    def search(self,data):
        # if you hit a leaf. IS IT JUST ONE LEAF??
        return False
        
LEAF = leaf()

class TwoNode:
    # if im adding values to the left or right it nneds to be in the parameter

    def __init__(self,data,left=LEAF,right=LEAF):
        # you asssigning leaf to self.left, but your able to pass any parameter values to left
        # here on the bottom
        self.data = data
        self.left = left
        self.right = right

    def count(self):
        # ^^^here you do self.right.count() which will call the count of the node, being whic
        # right or left, which could be one or zero in a two NODE
        return 1 + self.left.count() + self.right.count()
        

    def search(self, data):
        # ?!! its calling the self. data because there is
        # only one data tree(or is it only this data in the twoNode class
        #  its looking at..the self one correct?
        if data == self.data:
        # ANSWER DATA IS THE VALUE AND ITS REALLY CHECKING VALUE/DATA

            return True

        elif data < self.data:
            # this is recursion
            # CALLING another Nodes' search function 
            return self.left.search(data)
        else:
            return self.right.search(data)


class ThreeNode:
    def __init__(self,data1,data2,left=LEAF,middle=LEAF,right=LEAF):
        self.data1 = data1
        self.data2 = data2
        self.left = left
        self.middle = middle
        self.right = right
    def count(self):
        # dont need a if none check because you have the leaf class which makes it already to zero.
        return 2 + self.left.count() + self.right.count() + self.middle.count()
        # ^^tis isnt recursion its a fast way to count using leaf.
    def search(self,data):
        if data == self.data1 or data == self.data2:
            return True
        elif data < self.data1:
            return self.left.search(data)
        elif data < self.data2:
            return self.middle.search(data)
        else:
            return self.right.search(data)
        # ???!!!would this below still work cirrectly even though
        # I didnt have a else statement
        # elif data > self.data2:
        #     return self.right.search()
        # elif data < self.data1:
        #     return self.left.search()
        # elif data < self.data2:
        #     return self.middle.search()
class TwoThreeTree:
    def __init__(self,root = LEAF):
        self.root = root


        # this count at root will count 1 

    def count(self):
        return self.root.count()

    def search(self,data):
        # does this make the search function start at the root?
        return self.root.search(data)

# ITS not possible to print this!
EXAMPLE_TREE0 = TwoThreeTree()


EXAMPLE_TREE1 = TwoThreeTree(TwoNode(5))
print TwoThreeTree(ThreeNode(5,8,TwoNode(2))).count()
print EXAMPLE_TREE1.count()
# ^^here your printing the return

EXAMPLE_TREE2 = TwoThreeTree(ThreeNode(57,70, ThreeNode(52,55),
TwoNode(58),
ThreeNode(72,74)))

EXAMPLE_TREE3 = TwoThreeTree(
    ThreeNode(15,49,
    TwoNode(8,TwoNode(2), ThreeNode(11,14)),
    ThreeNode(21,38,ThreeNode(16,17), TwoNode(23),TwoNode(40)),
    EXAMPLE_TREE2.root))




