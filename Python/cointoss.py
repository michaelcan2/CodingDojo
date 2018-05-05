import random
heads = 0
tails = 0
for flip in range(3):
    result = random.randint(0,1)
    if result:
            result = "heads"
            heads += 1
    else:
            result = "tails"
            tails += 1
    print "Attempt #{} Throwing a coin...it's a {}! ... Got {} head(s) so far and {} tail(s) so far".format(flip,result,heads,tails)
print "Ending the program, Thank You!"
