sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

#method that detects if int is a big or small number
def intPrint(num):
    if num >= 100:
        print "That's a big number!"
    else:
        print "That's a small number"

#method that detects if string is long or small
def stringPrint(str):
    length = len(str)
    if length >= 50:
        print "Long sentence."
    else:
        print "Short sentence."

#method that detects if list is big or small
def listPrint(list):
    length = len(list)
    if length >= 10:
        print "Big list!"
    else:
        print "Short list."

intPrint(sI)
intPrint(mI)
intPrint(bI)
intPrint(eI)
intPrint(spI)
stringPrint(sS)
stringPrint(mS)
stringPrint(bS)
stringPrint(eS)
listPrint(aL)
listPrint(mL)
listPrint(lL)
listPrint(eL)
listPrint(spL)
