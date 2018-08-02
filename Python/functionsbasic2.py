# CORRECT!
# arr = [2,6,78,33,1]
# def printArr(arr):
#     for value in arr:
#         print value
# printArr(arr)


# def countdown(num):
#     arr=[]
#     for i in range(num, -1, -1):
#         arr.append(i)
#     return arr

# print countdown(5)


# 2 def printReturn([a,b]):
#     print(a)
#     return(b)
# printReturn([4,5])

#3 arr=[]
# def today(arr):
#     return sum arr[0] + arr.length

# print today(4,6,3,8)


# anagram python
# def ana(w1,w2): 
#     w2 = list(w2)
#     w1 = list(w1)
#     if len(w1) != len(w2):
#         return False
#     for i in w1:
#         if i in w2:
#             w2.remove(i)
#         else:
#             return False
#     return True

# print ana("star","rats"), " star and rats"
# print ana("star", "trash"), " star and trash"
# print ana("star", "strn"), " star and strn"
    
# problem 4
# def accept (arr):
#     newarr = []
#     for i in arr:
#         if i > arr[1]:
#             newarr.append(i)
        
#     return newarr
# newarr = accept([2,6,78,33,1])
# print len(newarr)
# print newarr
# prints 78 33 as there are 2 values greater then 6

# def lengthAndValue(size,value):
#     return len()


# use %s as a placeholder for strings and %d as a placeholder for numbers
hw = "Hello %s" % "world" 
py = "I love Python %d" % 3 
print(hw, py)
# the output would be: Hello world I love Python 3
# we can also pass variables


def high(name):
    name = name.split("a")
    # you needed to save the name.split to a variable which you did when you name=name.split("a")
    # otherwise you split it but did nothing with it and then you would print the original string.
    print("My name is %s" % (name))

high("michael")

def stairs(arr):
    max(arr)
    return stairs
print stairs([3,2,9])






# for i in range(30):
#     if not (i%3):
#         continue
#     print i
    # this prints only numbers that AREN'T multiples of 3.

# fiboSeq=[]
# a,b=0,1
# while(b<1000):
#     fiboSeq.append(a)
#     a,b=b,a+b
#     print fiboSeq