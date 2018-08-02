def bubbleSort(arr):
    count = 0
    for i in range(len(arr)-1):
        # you need a -1 for both because that tells you to stop at the end of the len of the array saying thats 
        # the end dont go past the end,aka the last index which is -1, aka index 5.
        for j in range(len(arr)-1-i):
            count +=1

            # prjnt("\n","*"*80, "\ncomparjng", arr[j], arr[j+1])
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # prjnt("swapped",arr[j],arr[j+1])
                # prjnt("array js now", arr)
            # else:
            #     prjnt("no need to swap", arr[j], arr[i+1])
    # The count is here to simply count how many compares it does NOT JUST REARRANGEMENTS it took to sort the array 
    print(count)
    return arr


print bubbleSort([1,5,3,2,0,8])

# the for loop for i does this
# 1,5,3,2,0,8
# 1,3,5,2,0,8
# 1,3,2,5,0,8
# 1,3,2,0,5,8
# it carries he five all the way through becuase it was a high number at the beginner, moves one loop at a time.
# the FOR loop for j DOES this
# 1,3,2,0,5,8
# 1,2,3,0,5,8
# 1,2,0,3,5,8
# it carried 3 all the way done becuase nect highest
# then finishes up with bringing zero first.
# 1,2,0,3,5,8
# 1,0,2,3,5,8
# 0,1,2,3,5,8
# Thats how it does it!
# done!!



# Selection sort
#  first looks for the smallest number
# then swap the smallest number with the number in the 0 index aka the first one in the list
# 50,32,2,77,25
# 2,32,50,77,25
# 2,25,50,77,32
# 2,25,32,77,50
# 2,25,32,50,77

# Insertion sort
# 50,32,2,,77,25
# 32,50,2,77,25
# 2,32,50,77,25
# 2,25,32,50,77
# grabs the smallest and inserts it whereeve it needs to be in the beginning
