info = {"name": "Marcus", "age": "21", "country": "United States", "language": "Java"}

def printDict(input):
    for key,data in input.items():
        if key == "name":
            print "My name is " + data
        elif key == "age":
            print "My age is " + data
        elif key == "country":
            print "My country of birth is " + data
        else:
            print "My favorite language is " + data

printDict(info)