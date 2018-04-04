def odd_even():
    for value in range(2001):
        if (value%2==0):
            odd_even = "even"
        else: 
            odd_even = "odd"
            print 'Number is {}. This is an {} number.'.format(value,odd_even)
    
odd_even()

def multiply(arr,num):
    for value in range(len(arr)):
         arr[value] *= num
    return arr

multiply([2, 4, 10, 16], 5)
