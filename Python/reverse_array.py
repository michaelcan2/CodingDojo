# def reverse(lst):
#     length = len(lst)
#     new_list = [None]*length
#     for i in lst:
#         length = length - 1
#         new_list[length] = i
#     print new_list

# reverse([3,4,2,5])



# countdown algorithm practice

# def countDown(num):
#     arr=[]
#     x=num
#     while x>=0:
#         arr.append(x)
#         x=x-1
#     print(arr)
# countDown(5)

# def countDown(num):
#     arr=[]
#     x=num
#     while x >= 0:
#         arr.append(x)
#         # this literally makes x count down to zero b/c its in a loop
#         x= x-1
#     print(arr)

# countDown(3)



def countDown(n):
    arr = []
    while n >= 0:
        arr.append(n)
        n -=1
    print arr

countDown(3)


use for loop to print all od them 
car = car 