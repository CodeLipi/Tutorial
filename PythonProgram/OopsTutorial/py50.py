# public, private, protected variables

class Test:
    # def __init__(self):
    #     self.x = 19
    # def m1(self):
    #     self.x = 19
    def __init__(self):
        self.__x = 19   # private
    def m1(self):
        print(self.__x)

t = Test()
# t.m1()
# print(t.x)

# print(t._Test.__x)  # not accessed by using this method also