#multiples pt1
for val in range(1, 1000):
    if val%2 == 1:
        print val

#multiples pt2
for val in range(5, 1000001):
    if val%5 == 0:
        print val

#sum List
a = [1, 2, 5, 10, 255, 3]
length = len(a)
sum = 0;
for val in range(0, length):
    sum += a[val]
print sum

#average list
for val in range(0, length):
    average = sum/length
print average