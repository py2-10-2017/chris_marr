class Patient(object):
    def __init__(self, id_number, name, allergies, bed_number = -1):
        self.id = id_number
        self.name = name
        self.allergies = allergies
        self.bed_number = bed_number
    def set_bed_number(self, bed_number):
        self.bed_number = bed_number
        return self
    def display_all(self):
        print "ID:", self.id
        print "Name:", self.name
        print "Allergies:", self.allergies
        print "Bed Number:", self.bed_number
        print " "
        return self
class Hospital(object):
    def __init__(self, patients, name, capacity = 3):
        self.patients = patients
        self.name = name
        self.occupancy = len(self.patients)
        self.beds = []
        for i in range(capacity):
            self.beds.append(-1)
    def admit(self, patient):
        if self.occupancy < len(self.beds):
            for i in range(len(self.beds)):
                if self.beds[i] == -1:
                    print "admited", i                   
                    self.patients.append(patient)
                    self.beds[i] = i
                    self.occupancy += 1     
                    return i
        else:
            print "rejected"
        return -1
    def discharge(self, patient):
        for i in range(len(self.beds)):
            if self.beds[i] == patient.bed_number:
                print "discharged", i
                patient.set_bed_number(0)
                self.patients.pop(0)
                self.beds[i] = -1
                self.occupancy -= 1   
                return i
        return self
    def display_all(self):
        print "Patients:", len(self.patients)
        print "Name:", self.name
        print "Capacity:", len(self.beds)
        print "Occupancy:", self.occupancy
        print " "
        return self
print " "
p1 = Patient(1, "Mau", "most drugs").display_all()
p2 = Patient(2, "Alex", "apples").display_all()
p3 = Patient(3, "Santi", "sugar").display_all()
p4 = Patient(4, "Gerardo", "none").display_all()
h = Hospital([],"General Hospital")

bed_number = h.admit(p1)
if bed_number >= 0:
    p1.set_bed_number(bed_number)

bed_number = h.admit(p2)
if bed_number >= 0:
    p2.set_bed_number(bed_number) 

bed_number = h.admit(p3)
if bed_number >= 0:
    p3.set_bed_number(bed_number) 

h.display_all()

bed_number = h.admit(p4)
if bed_number >= 0:
    p4.set_bed_number(bed_number) 

h.display_all()

h.discharge(p1)

h.display_all()

bed_number = h.admit(p4)
if bed_number >= 0:
    p4.set_bed_number(bed_number) 

h.display_all()