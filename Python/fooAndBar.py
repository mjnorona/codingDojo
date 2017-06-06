 

def prime(num):
    isPrime = True
    for j in range(2, num/2):
        if (num % j == 0):
            isPrime = False
            break
    return isPrime

def squaresList(begin, end):
    arr = []
    for i in range(begin, end + 1):
        arr.append(i*i)
    return arr

def fooBar():
    arr = squaresList(10, 316)
    for i in range(100, 100001):
        isSquare = False;
        for j in range (0, len(arr)):
            if arr[j]==i:
                isSquare = True
        if prime(i) == True:
            print str(i) + " Foo"
        elif isSquare == True:
            print str(i) + " Bar"
        else:
            print str(i) + " FooBar"
        
#10 to 316
#squaresList(10, 316)
fooBar()
