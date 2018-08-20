# question for algos do you expect students to use method that exist or go the log way and 
# acgually write the algo out for say .append or .push

# when should we stop and think is there a method for that....while working thru probelms???
# def reverseString(str):
#     word = ""


#  not sure how to grab the last index in the length in python
# also in a python for loop not sure how to decrement go down
# for loop in python only grabs the object not the index!!!
# enumerate cant work through a string
# lambdas are variables name that only exist in little block of code
# for i in range(str):
#     word += str[i]
# return word


#     for i,val in enumerate(str):
#         word += str[len(str)-i-1]
#         print val
#     return (word)

   


# print(reverseString("today"))


# def evenLength(arr):
#     result = []
    # cant iterate over a length but range can
    # for i in arr:
    #     if(len(i) % 2 == 0):
    # do if(len(i) % 2 != 0): for odds
           
#             result.append(i)
#     return result 

# print(evenLength(['hello', 'so', 'do', 'i', 'yay!']))


def parensValid(str):
    open = 0
    close = 0
    for i in range(len(str)):
        # cant be enumerate go over with josh after 11am lecture
        if(str[i] == '('):
            open += 1
        
        if(str[i] == ')'):
            if(open <= close):
                return False
            close +=1
    if(close != open):
        return False
    else:
        return True

print(parensValid('(whatup)world()'))



# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None



    
            