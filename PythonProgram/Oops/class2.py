class Student:
    def __init__(self):   # constructor ; this is must imp for object creatiion
        print('Constructor Execution ...')
        self.name = 'kush'
        self.rollno = 101
        self.marks = 99

    def talk(self):
        print('Hello I am ',self.name)
        print('My roll no is ',self.rollno)
        print('I got marks : ',self.marks)

s1 = Student()   # s is reference var, also s (obj) is created
s2 = Student()

print(s1.name)
print(s1.rollno)
print(s1.marks)   # accessing properties by reference variables

s1.talk()  # accessing method by reference variables

# both object are different
print(id(s1))
print(id(s2))
