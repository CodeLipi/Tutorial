class Student:
    # def __init__(self,x,y,z):   # constructor 
    #     # print('Constructor Execution ...')
    #     self.name = x
    #     self.rollno = y
    #     self.marks = z

    def __init__(self,name,rollno,marks):   # special method (consructor)
        self.name = name        # instance variable; self.name, self.rollno, self.marks
        self.rollno = rollno
        self.marks = marks

    def talk(self):     # instance method
        print('Hello I am ',self.name)
        print('My roll no is ',self.rollno)
        print('I got marks : ',self.marks)

s1 = Student('John', 34, 90)
print('Student 1 : ', s1.name, s1.rollno, s1.marks)

s2 = Student('Jenny', 44, 70)
print('Student 2 : ', s2.name, s2.rollno, s2.marks)