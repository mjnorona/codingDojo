def multiplicationTable():
    print "{:>3}".format("x"),
    for i in range(1,13):
        print "{:>3}".format(str(i)),
    print ""
    for i in range(1,13):
        print "{:>3}".format(str(i)),
        for j in range(1,13):
            print "{:>3}".format(str(j*i)),
        print ""


multiplicationTable()
