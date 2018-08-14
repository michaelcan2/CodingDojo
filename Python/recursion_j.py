import math
# def fact(n):
#     if n<0:
#         return -1
#     elif n < 2:
#         return 1
#     else:
#         # this part is recursion its doing 6*5*4*3*2*1
#         # i'm confused on how did it know i wanted to start a recursion it's running like a loop
#         # but there's no specific syntax that is doing it like a while or for loop
#         return n * fact(n-1)
#         # is it the if statement? if the number is >2 less then 2 then call the function again...hmmm.
#         # and so it knows to keeps foinf again wit h4 then 3 then 2 b/c the if statemtn and will ultimately be 6*120
# print(fact(6))


# def fact(n):
#     if n <0:
#         return -1
#     elif n < 2:
#         return 1
#     else:
#         return n * fact(n-1)

# print(fact(6))


# def factorial( n ):
#    if n <1:   # base case
#        return 1
#    else:
#        returnNumber = n * factorial( n - 1 )  # recursive call
#        print(str(n) + '! = ' + str(returnNumber))
#        return returnNumber

# print(factorial(6))



# thi is still noy eotking
# this is like factorial but adding 5+4+3+2+1
# def sigma(x):
#     x =int(math.floor(x))
#     if x == 0:
#         return 0
#     return x + sigma(x-1)

# print(sigma(1.8))


def rSigma(num):
    returnVal = 0
    # if the input is greater then or equal to 1, then do this.
    if(num >= 1):
        # here your making whatever num is into an integer
        intNum = math.trunc(num)
        # here your setting a variable of the one number less then the number you inputted
        # also you ** are recalling the function and it will keep going till its 1 because of the if statement
        # and will also include 1 because it is less then and EQUAL TOO
        # 3+2+1
        prevVal = rSigma(intNum-1)

        returnVal = prevVal + intNum
    return returnVal

print(rSigma(4))


