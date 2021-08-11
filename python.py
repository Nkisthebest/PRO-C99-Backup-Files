mark = input()
class student(object):
    def __init__(self,name,roll,section,marks):
        self.name = name
        self.roll = roll
        self.self = section
        self.marks = marks
    def displaymarks(self):
        print(self.marks)
    def total(self):
        print(self.marks[0]+self.marks[1]+self.marks[2])
    def average(self):
        print((self.marks[0]+self.marks[1]+self.marks[2])/3)
john = student("John",25,10,[10,20,30])
john.total()
john.average()