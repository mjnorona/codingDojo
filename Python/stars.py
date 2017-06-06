def draw_stars(list):
    for i in range(0, len(list)):
        stars = ""
        for j in range (0, list[i]):
            stars += "*"
        print stars

x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)

def draw_stars2(list):
    for i in range(0, len(list)):
        text = ""
        if type(list[i]) == int:
            for j in range(0, list[i]):
                text+= "*"
        elif type(list[i]) == str:
            for j in range(0, len(list[i])):
                text += list[i][0].lower()
        print text

y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars2(y)

