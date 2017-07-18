class Student:
    def __init__(self,sname,sno):
        self.sname=sname
        self.sno=sno
    def Disp(self):
        print "Name of Student ", self.sname, ", his roll is ", self.sno
Student1 = Student("Nikesh", 650)
Student2 = Student("Python", 302)
Student1.Disp()
Student2.Disp()
