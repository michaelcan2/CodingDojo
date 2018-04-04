'''
fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce','cucumber','carrots']

fruits_and_vegetables = fruits + vegetables
print fruits_and_vegetables 
salad = 3 * vegetables
print salad
'''
'''
drawer = ['documents', 'envelopes','pens']
print drawer[0]

print drawer[1]
'''
'''
count = 0
while count < 5:
    print 'looping -', count
    count += 1
'''
'''
for count in sequence(0,5):
    print "looping", count
'''
'''
the find method
words = "It's thanksgiving day. It's my birthday,too!"
words.find("day")
print words.find('day')
'''

'''
words ="It's thanksgiving day. It's my birthday,too!."
print words.replace('day','month')
'''

'''
x = [2,54,-2,7,12,98]
min(x)
print min(x)

x = [2,54,-2,7,12,98]
max(x)
print max(x)
'''
'''
x = ["hello",2,54,-2,7,12,98,"world"]
first = x[0]
last= x[-1]
print [first, last]
'''
'''
x = [19,2,54,-2,7,12,98,32,10,-3,6]
y = sorted(x)
print y

'''
'''
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
'''
'''
x = ["hello",2,54,-2,7,12,98,"world"]
print x[:3]

# : <-- is the beginning or the the end depending if your number is on the left or right of it.
'''

x = [19,2,54,-2,7,12,98,32,10,-3,6]
y= x[:len(x)/2]
z= x[len(x)/2:]
print y
print z

x=[y]+z

print