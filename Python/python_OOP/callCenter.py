class Call(object):
    def __init__(self, id, name, number, time, reason):
        self.id = id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason

    def display(self):
        print "ID: " + self.id
        print "Name: " + self.name
        print "Phone Number: " + self.number
        print "Time of Call: " + self.time
        print "Reason for Call: " + self.reason
        print ""

class CallCenter(object):
    def __init__(self, calls):
        self.calls = calls
        self.queue = len(calls)

    def add(self, id, name, number, time, reason):
        self.calls.append(Call(id, name, number, time, reason))
        return self

    def remove(self):
        for i in range(0, len(self.calls)-1):
            self.calls[i] = self.calls[i+1]
            self.calls = self.calls[:-1]

        return self

    def info(self):
        for i in range(0, len(self.calls)):
            print "Name: " + self.calls[i].name
            print "Phone Number: " + self.calls[i].number
        print "Queue length: " + str(self.queue)
        print ""

call = Call("908938", "Marcus", "9802039222", "2:00pm", "Wanted to talk")
call.display()

call1 = Call("098341", "Marcus", "9802039222", "2:00pm", "Wanted to talk")
call2 = Call("923462", "Gemma", "7073948572", "3:00pm", "Wanted to talk")
call3 = Call("184729", "Jazzerine", "1039482736", "4:00pm", "Wanted to talk")
call4 = Call("110294", "Patient", "4958372846", "5:00pm", "Wanted to talk")

calls = [call1, call2, call3, call4]
center = CallCenter(calls)
center.info()