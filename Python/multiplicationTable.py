def multiplicationTable():
    firstRow = "x    1 2 3 4 5 6 7 8 9 10 11 12"
    print firstRow
    for i in range(1,13):
        row = str(i) + "    "
        for j in range(1,13):
            row += str(j*i) + " "
        print row

multiplicationTable()