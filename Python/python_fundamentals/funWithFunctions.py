#function that detects if a number is even/odd up to 2000
def odd_even():
    for i in range(0, 2001):
        output = "Number is " + str(i) + ".  This is an "
        if i % 2 == 0:
            output += "even number."
        else:
            output += "odd number."
        print output

#function that multiplies each list value by an integer
def multiply(arr, num):
    for i in range(0, len(arr)):
        arr[i] = arr[i] * num
    return arr

odd_even()
a = [2,4,10,16]
b = multiply(a, 5)
print b