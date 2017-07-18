class Room:
    def __init__(self,ht,w):
        self.height = ht
        self.width = w
    def Area(self):
        return self.height*self.width
class Child(Room):
    def __init__(self,ht,w,l):
        Room.__init__(self,ht,w)
        self.length=l
    def Vol(self):
        return self.Area()*self.length

p = Room(30,40)
q = Child(45,60,65)

print(p.Area())
print(q.Vol())
