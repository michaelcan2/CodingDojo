class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
class AvlTree:
    # the root is the parent node, you need to input the parent node 
    # root is the cur_node
    def insert(self,root,key):
        # ??how do we know this root is a node
        # may need to change self.root
        # if not root:
        # if self.root == None:
        if not root:
            return TreeNode(key)
        elif key < root.val:
            # at the end. when there is no root.left this new key becomes root.left
            # the root.left will ultimate equal a node.
            root.left = self.insert(root.left,key)
            # root.left = TreeNode(key)
        else: 
            root.right = self.insert(root.right,key)

        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        if balance < 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

        
        # now after we inserted it here we doubled check if it violates the AVL tree
        # root.height is the parent node still, above the root.left, and root.right 
        # would be the child for the root.height.

        def getHeight(self,root):
            if not root:
                return 0
            # these are only compaing the heights of the SUBTREEE just a check of how many there are
            # the max would be 2 or 1 or 0
            return self.getHeight(root.left)-self.getHeight(root.right)

        root.height = 1 + max(self.getHeight(root.left),
        self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)


class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AvlTree:
    def insert(self,root,key):
        if not root:
            return Node(value)
        elif value < root.val:
            root.left = self.insert(root.left,value)
        else:
            root.right = self.insert(root.right,value)

    # this get height makes no sense how is it keeping track of the height??
    def getHeight(self,root):
        if not root:
            return 0
        
        else:
            return root.height

        root.height = + 1 max(self.getHeight(root.left),self.getHeight(root.right))

        balance = self.getBalance(root)

        def getBalance(self,root):
            if not root:
                return 0
            return self.getHeight(root.left) - self.getHeight(root.right)
    ``
        





    
