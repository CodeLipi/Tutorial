class Student:

    college = 'BIT'   # static variable
    director = 'Dkotery'

    def __init__(self, name, rollno):  # special method (constructor)
        self.name = name        # instance variable
        self.rollno = rollno        # instance variable

        # self.name, self.rollno is instance variable while name, rollno is dummy variable which holds the value.

    def get_student_info(self):   # instance method
        greet = 'Welcome here...'    # local variable
        print('Student Name : ',self.name)
        print('Student rollno : ',self.rollno)

    @classmethod
    def get_collage_info(cls):   # class method
        print('Collage Name : ',cls.college)
        print('Director Name : ',cls.director)

    @staticmethod
    def m1():   # static method
        x = 10      # local variable
        for i in range(x):   # i is local variable
            print(i)


s = Student("kush",23)

s.get_student_info() # accessing instance method

Student.get_collage_info()  # accessing class method

Student.m1() # accessing static method
