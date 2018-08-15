def print1to255():
    for i in range(1,256):
        print i

print1to255()

def print_odds_1_to_255():
    for i in range(1,256,2):
        print i

print_odds_1_to_255()

def print_ints_and_sum():
    sum = 0
    for i in range(256):
        sum += i
        print i
    print sum

print_ints_and_sum()

def print_array_value(arr):
    for values in arr:
        print values

print_array_value(['mike','liz','steve', "i am a having a good day"])

def maximum_array(arr):
    print max(arr)

print (maximum_array([44,12,67]))

def find_average(arr):
    print (sum(arr)/len(arr))

find_average([5,2,7])

def return_odds():
    new_array=[]
    for i in range(1,256,2):
        new_array.append(i)
    print new_array

return_odds()

def square_array_value(arr):
    for item in range(len(arr)):
        arr[item] *= arr[item]
    print arr

square_array_value([3,5,8,9])

def greater_than_y(arr, y):
    count = 0
    for item in arr:
        if item > y:
            print item
            count += 1
    print count

greater_than_y([2,3,4,5], 3)

def zero_out_negatives(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = 0
    print arr

zero_out_negatives([0,5,-2,-7,8])
def max_min_avg(arr):
    print [max(arr), min(arr), (sum(arr)/len(arr))]

max_min_avg([5,6,7])

def shift_arry(arr):
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = 0
    print arr
        
shift_arry([2,4,5,6,4])

def swap_string(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = 'Dojo'
    print arr

swap_string([-1,-2,3,4,-5])
