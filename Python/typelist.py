l = ['magical unicorns',19,'hello',98.98,'world']
la = [2,3,1,7,4,12]
lb = ['magical','unicorns']
# isinstance is saying (this is the VALUE), next you are checking if the value is  STR or a INT
def typeList(list):
    string = ''
    num = []
    for i in list:
        if isinstance(i, str):
            string += i
            string += ' '
        else:
            num.append(i)
    if len(string) > 0 and len(num) > 0:
        print "The list you entered is of mixed type"
        print "String: " + string
        print "Sum: " + str(sum(num))
    elif len(string) > 0:
        print "The list you entered is of string type"
        print "String: " + string
    else:
        print "The list you entered is of integer type"
        print "Sum: " + str(sum(num))

typeList(l)