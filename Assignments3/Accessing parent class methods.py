class Base:
    def __init__(self):
        print "call the base class"
    def getString(self,string):
        self.string=raw_input()
    def printString(self,uppercase):
        self.uppercase = self.string.upper()

class Child(Base):
    def __init__(self,string,uppercase):
        Base.__init__(self,string,uppercase)
Child.getString()
Child.printString()