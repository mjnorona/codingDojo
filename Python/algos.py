def parensValid(string):
    count = 0
    valid = True
    for i in range (0, len(string)):
        if string[i] == "(":
            count += 1
        elif string[i] == ")":
            count -= 1
        if count == -1:
            valid = False
            break
    if count != 0:
        valid = False
    return valid

print "String is: " + str(parensValid("((())"))
print "String is: " + str(parensValid("())"))
print "String is: " + str(parensValid("((()))()"))