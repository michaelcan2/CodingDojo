class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
         if(self.items != None):
             return self.items[-1]
        # if not self.is_empty():
        #     return self.items[-1]
        
    def get_stack(self):
        return self.items


s= Stack()
print(s.is_empty())
s.push("A")
print(s.is_empty())
s.push("B")
s.push("C")
s.pop()
print(s.is_empty())
print(s.peek())

# courses = ['History', 'Math', 'Physics', 'Comp']
# num = [1,2,3,4,5]

# courses.insert(0,'art')
# courses.sort()
# how can I sort then with art being included as well?

# print(courses)
# print(sum(num))