name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
    new_dict = {}
    for i in range(0, len(arr1)):
        new_dict[arr1[i]] = arr2[i]
    # your code here
    return new_dict

print make_dict(name, favorite_animal)
