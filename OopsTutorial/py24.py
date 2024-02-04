# getter and setter method

class Student:
    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name
    
    def setMarks(self,marks):
        self.marks = marks

    def getMarks(self):
        return self.marks
    
# s = Student()

# s.setName('kush')
# print(s.getName())

# s.setMarks(90)
# print(s.getMarks())

n = int(input('Enter no of students : '))

for i in range(n):
    s = Student()
    name = input('Enter name : ')
    marks = int(input('Enter marks :' ))

    s.setName(name)
    s.setMarks(marks)

    print('hi',s.getName())
    print('Your marks : ',s.getMarks())
    print()
