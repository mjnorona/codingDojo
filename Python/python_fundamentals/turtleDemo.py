import turtle

# the distance we want the pointer to travel each time
DIST = 100
for x in range(0,6):
    print "x", x
    for y in range(1,5):
        print "y", y
        # turn the pointer 90 degrees to the right
        turtle.left(90)
        turtle.right(5)
        # advance according to set distance
        turtle.forward(DIST)
    # add to set distance
    DIST += 20