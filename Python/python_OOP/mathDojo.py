class MathDojo(object):
    def __init__(self):
        self.value = 0

    def add(self, *args):
        sum = 0
        for i in range(0, len(args)):
            if type(args[i]) == int:
                #print "is int"
                sum += args[i]
                #print sum
            else:
                miniSum = 0
                #print "is list or tuple"
                for j in range(0, len(args[i])):
                    miniSum += args[i][j]
                sum += miniSum
        self.value += sum
        return self

    def subtract(self, *args):
        sub = 0
        for i in range(0, len(args)):
            if type(args[i]) == int:
                # print "is int"
                sub -= args[i]
            else:
                miniSum = 0
                #print "is list or tuple"
                for j in range(0, len(args[i])):
                    miniSum += args[i][j]
                sub -= miniSum
        self.value += sub
        return self

    def result(self):
        print self.value
        return self

MathDojo().add(2).add(2, (5,3)).subtract(3, 2).result()