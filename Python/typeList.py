

def printList(list):
    elType = type(list[0])
    mixed = False
    text = ""
    sum = 0;

    for i in range(0, len(list)):
        if type(list[i]) is not elType:
            mixed = True

        if type(list[i]) is float or type(list[i]) is int:
            sum += list[i]
        elif type(list[i]) is str:
            text += list[i] + " "
    
    if mixed is True:
        print "The array you entered is of mixed type"
        print "String: " + text
        print "Sum: " + str(sum)
    else:
        if elType is int:
            print "The array you entered is of integer type"
            print "Sum: " + str(sum)
        elif elType is str:
            print "The array you entered is of string type"
            print "String: " + text
    
l = ['magical unicorns',19,'hello',98.98,'world']
printList(l)

k = [2,3,1,7,4,12]
printList(k)

j = ['magical','unicorns']
printList(j)

