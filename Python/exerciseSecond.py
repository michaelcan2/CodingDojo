import random

# def beCheerful(name="",repeat=2):
#     print ("hello {} ".format(name)*repeat)


# beCheerful(name = "Michael", repeat = 6)

# print round((random.random()*100))

# print random.randint(1,100)

# x=[[5,2,3], [10,8,9]]

# `students = [
#     {'first_name': 'Michael', 'last_name':'Jordan'},
#     {'first_name': 'John', 'last_name' : 'Rosales'}
# ]`
# students['last_name']='Bryant'

# print(students[0])

# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# def part1(dict):
#     a=0
#     while a<len(dict):
#         table=[]
#         sum=''
#         i=0
#         for val in dict[a].values():
#             table.append(val)
#             sum=sum+table[i]+' '
#             i=i+1
#         a=a+1
#         print(sum)
# part1(students)


# def number():
#     for i in range(1,256):
#         print(i)


# def number3():
#     sum = 0
#     for i in range(0,256):
#         sum += i
#         print(i, sum)



# def num():
#     sum=0
#     for i in range(0,256):
#         sum+=i
#         print (i, sum)


# def number4(myList):
#     for item in myList:
#         print(item)

# print number4([4,7,9,8])

# def number5(myList):
#     max = myList[0]
#     for item in myList:
#         if max < item:
#             max = item
#     return max

# print number5([6,5,8,9])

# def number6(myList):
#     sum = 0.0
#     for item in myList:
#         sum += item
#     return float(sum / len(myList))

# print number6([7,8,6,4])



# yay! put the number 1 to 255 into an array.
# def number7():
#     lst = []
#     for i in range(1,256,2):
#         lst.append(i)
#     return lst

# print number7()



# mulitply all numbers in the list by themse;eves and return them 
# def number8(myLst):
#     i = 0
#     while i<len(myLst):
#         myLst[i] *= myLst[i]
#         i += 1
#     return myLst

# def number8(lst):
#     i = 0
#     while i < len(lst):
#         lst[i]*=lst[i]
#         i+=1
#     return lst

# def number8(lst):
#     i=0
#     while i < len(lst):
#         lst[i]*=lst[i]
#         i+=1
#     return lst

# def number8(lst):
#     i = 0
#     while i < len(lst):
#         lst[i]*lst[i]
#         print lst
#         i+=1

# print number8([5,8,3,6])

# YAY!! if there are any # greater then y count them, then return count used a for loop 
# def number9(myLst, y):
#     count = 0
#     for item in myLst:
#         if item > y:
#             count += 1
#     return count

# print number9([3,5,6,2], 4)

# if number is negative turn to zero YESSS!!!
# def number10(myLst):
#     i = 0
#     while i < len(myLst):
#         if myLst[i] < 0:
#             myLst[i] = 0
#         i += 1
#     return myLst






# cant understand what this does
# def number12(myLst):
#     i = 0
#     while i < len(myLst)-1:
#         myLst[i] = myLst[i+1]
#         i+=1
#     myLst[len(myLst)-1] = 0
#     return myLst

# print number12([2,1,8,3])

# YAY!! 13 done
# def number13(myLst):
#     # this i is the index on where to start in the WHILE loop
#     i = 0
#     while i < len(myLst):
#         the bracket are when your looking at a specfic index not moving through it
#         if myLst[i] < 0:
#             myLst[i] = "Dojo"
#         i += 1
#     return myLst



# def number13(lst):
#     i=0
#     while i < len(lst):
#         if lst[i] < 0:
#             lst[i] = "DOJO"
#         i+=1
#     print lst

# print number13([1,-2,3,-4])

# changed the last_name from Jordan to Bryant
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]

# students[0]['last_name']='Bryant'

# print students 
# print fxn():

# def number13(arr):
#     max = 0
#     for i in arr:
#         if i > max:
#             max = i
#     print max

# number13([4,6,8,7])

# def swap(arr):
#     arr[0], arr[1] = arr [1], arr [0]
#     print arr


# print swap[2,3]

# def bubble(arr):
#     for i in range(len(arr)):
#         print("index", i, "value",arr[i])
#         print("comparing", arr[i], arr[i+1])
#         if arr[i] > arr[i+1]:
#             arr[i], arr[i+1] = arr[i+1], arr[i]
#             print("swapped",arr[i],arr[i+1])
#         else:
#             print("no need to swap")


# bubble([1,3,5,2,0,8])

def reverse(lst):
    length = len(lst)

    # [none] creates an empty list, when you *length to none your just copying inth the empty array everything
    # that is in length aka what you multiplied by
    # now new_list will have the length of 4, just like the original you made
    new_list = [None]*length
    for i in lst:
        # in a for loop -1 is subtracting by an index not just by 1
        # back one index at a time 
        # so it was 3 and now 2.
        length = length - 1
        new_list[length] = i
    print new_list

reverse([3,4,2,5])

# def rev(arr):
#     s = len(arr)
#     new_arr = s
#     for i in arr:
#         new_arr[s] = i
#     print new_arr

# print rev([3,4,2,5])
