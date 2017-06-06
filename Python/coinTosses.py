import random

def coinToss():
    heads = 0
    tails = 0
    for i in range(1, 5001):
        output = "Attempt #" + str(i) + " Throwing a coin... It's a "
        toss = random.randint(1, 2)
        if toss == 1:
            heads += 1
            output += "head! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
        else:
            tails += 1
            output +="tail! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
        print output
    print "Ending the program, thank you!"

coinToss()
