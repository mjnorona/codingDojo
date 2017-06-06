def checkerboard():
    for val in range(0, 8):
        if val % 2 == 0:
            print "* * * * "
        else:
            print " * * * *"

checkerboard()