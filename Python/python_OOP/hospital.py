class Patient(object):
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bedNum = None

    def setBedNum(self, num):
        self.bedNum = num
        return self

    def displayPatient(self):
        print "ID: " + self.id
        print "Name: " + self.name
        print "Allergies: " + self.allergies
        print "Bed Number: {}".format(self.bedNum)
        print ""
        return self

pat = Patient("009847", "Marcus", "peanuts")
pat.displayPatient()



class Hospital(object):
    def __init__(self, patients, name, capacity):
        self.patients = patients
        self.name = name
        self.capacity = capacity

    def admit(self, id, name, allergies, bedNum):
        if len(self.patients) < self.capacity:
            self.patients.append(Patient(id, name, allergies))
            self.patients[len(self.patients) - 1].setBedNum(bedNum)
            print "Patient is admitted"
        else:
            print "Hospital is full"
        return self

    def displayHospital(self):
        print "Name: " + self.name
        print "Capacity: " + str(self.capacity)
        print ""

        return self

pat1 = Patient("002842", "Marcus", "peanuts")
pat2 = Patient("001028", "Gemma", "cats")
pat3 = Patient("001049", "Jazz", "dogs")
pat4 = Patient("002748", "Paciencia", "people")

patients = [pat1, pat2, pat3, pat4]
hosp = Hospital(patients, "Sutter", 5)
hosp.displayHospital()
hosp.admit("029341", "John", "meat", 6)
hosp.admit("003841", "Jameson", "dairy", 7)




