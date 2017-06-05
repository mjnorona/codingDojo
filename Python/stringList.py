#find and replace
words = "It's thanksgiving day. It's my birthday, too!"
print words.find("day")

#min and max
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

#first and last
y = ["hello",2,54,-2,7,12,98,"world"]
count = len(y)
first = y[0]
last = y[count - 1]
print first
print last

#new list
z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
b = []
length = len(z)/2
a = z[0:length]
print a
b.append(a)
b.extend(z[length: len(z)])
print b
