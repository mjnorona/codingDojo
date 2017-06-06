import random

def scoresAndGrades():
    print "Scores and Grades"
    for i in range(0, 10):
        score = random.randint(60, 100)
        output = "Score: "
        if score >= 90:
            output += str(score) + "; Your grade is A"
        elif score >=80 and score < 90:
            output += str(score) + "; Your grade is B"
        elif score >= 70 and score < 80:
            output += str(score) + "; Your grade is C"
        else:
            output += str(score) + "; Your grade is D"
        print output
    print "End of the program. Bye!"

scoresAndGrades()