age = 17

# if age > 15:
#     print('age is greater than 15')

# for i in range(50):
#     print ('i is', i)

def sum(a,b):
    print("a", a, "b:",b)
    return a+b

print sum(1,5)

print(sum(2,4)+sum(1,5))

def say_hello(name=""):
    if name:
        print('Hello, '+name+', from inside this function')
    else:
        print('No name')
    