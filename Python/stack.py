# all your comments may have MESSED THIS UP!!
class Stack:
    def __init__(self):
        # we defined a class variable called items
        # ---you can tell its a class var by the self.
        # we've defined self.items to an empty list
        # ???the list is created when we create a stack object.
        self.items = []
        # in this case the item was the book.
    def push(self,item):
        # we want to push w/e item we are given to the top of the stack. to do this we type.
        self.items.append(item)
        # ^^^this says add w/e we input for item into the list called items
        # append adds to the end of the list.
    def pop(self):
        # since there already is a built in method, why did they make a 
        # a function with the method.
        return self.items.pop()
        # ^^^this simply means do this.
        # this will return to us the top element of the stack.
    def peek(self):
        # this fxn tells us what is on the top of the stack aka
        # THE END OF THE LIST
        if(self.items != None):
            # the specific piece that is the this list 
            # is it NOT THE CLASS 
            return self.items[-1]



    def is_empty(self):
        # this == will have a boolean output
        return self.items == []
    def get_stack(self):
        return self.items


# Below is your new easy understandbale way by doing.
# class Stack:
#     def __init__(self):
#         self.root = []

#     def push(self,data):
#         return self.root.append(data)

#     def pop(self):
#         return self.root.pop()

#     def get(self):
#         return self.root

#     def empty(self):
#         if self.root == []:
#             return True
#         else:
#             return False

#     def peek(self):
#         if self.root != None:
#             return self.root[-1]

thing = Stack()


thing.push(1)
thing.push(2)
thing.push(3)


print thing.peek()














