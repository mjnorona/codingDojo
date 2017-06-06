def compArr(arr1, arr2):
    if (len(arr1) != len(arr2)):
        print "The lists are not the same"
    else:
        boo = True
        for i in range(0, len(arr1)):
            if arr1[i] != arr2[i]:
                boo = False
                break
        
        if boo is True:
            print "The lists are the same"
        else:
            print "The lists are not the same"

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
compArr(list_one, list_two)

list_three = [1,2,5,6,5]
list_four = [1,2,5,6,5,3]
compArr(list_three, list_four)

list_five = [1,2,5,6,5,16]
list_six = [1,2,5,6,5]
compArr(list_five, list_six)

list_seven = ['celery','carrots','bread','milk']
list_eight = ['celery','carrots','bread','cream']
compArr(list_seven, list_eight)

