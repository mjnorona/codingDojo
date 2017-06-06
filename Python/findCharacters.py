# string = "value"
# if string[0] == "a":
#     print True
# else:
#     print False
def findChar(list, character):
    newList = []
    for i in range(0, len(list)):
        if (list[i].find(character) != -1):
            newList.append(list[i])
    return newList

# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = ['hello','world']

print findChar(word_list, char)

