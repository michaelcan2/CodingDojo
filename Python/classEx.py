class Robot:
    # below is the constructor
    def __init__(self,name,color,weight):
        # when you first create an object of this type. call this function
        self.name = name
        self.color = color
        # you call these when you want to call a specific attribute within an instance
        self.weight = weight
    # when we have a function in a class, when the function is a method of a clas
    #  we must include SELF in the parathesis as an argument, the self is the same as self.name
    # it's a PLACEHOLDER to say any object(object being ("tom, "red",30)) we make can use the init constuctor and
    # as well as the function. 
    # self simply refers to the single instance of the class, the entirely of what a class has made
    # r1 = Robot("Tom", "red", 30)
    def introduce_self(self):
        print("My name is "+ self.name)
        print("My favorite color is " +self.color)
        print(self.weight)
# self refers to whatever object we are running this on which is r1! 
# but if its self.name self is Tom, the name

r1 = Robot("Tom", "red", 30)
# it'll set tom as its name as in the argument on line 3 and on line 4 will connect with self.name
# this r1 is calling the __init__ method
r2 = Robot("jim","blue",40)

class Person:
    def __init__(self,n,p,i):
        self.name = n
        self.personality = p
        self.is_sitting=i

    def sit_down(self):
        self.is_sitting=True

    def stand_up(self):
        self.is_sitting=False

p1 = Person("Alice", "aggressive", False)
p2 = Person("becky", "talkative", True)

p1.robot_owned =r2
p2.robot_owned = r1

p1.robot_owned.introduce_self()
# r1.introduce_self()
# r2.introduce_self()


# l=[3,9,4,6]

# print min(l)
# print max(l)
# l.append(2)
# # [3,9,4,6,2]
# l.pop(0)
# # pop method take off the last index unless specified which in this case takes out the first index.
# # [9,4,6,2]
# print l
# l.reverse()
# print l
# l.sort()
# print l