# Duck typing
class Duck:
    def talk(self):
        print('Quack..Quack...')

class Dog:
    # def talk(self):
    #     print('Bow..Bow..')
    # pass    # raise AttributeError
    def bark(self):
        print('Bow..Bow..')

class Cat:
    def talk(self):
        print('Meow..Meow..')

class Goat:
    def talk(self):
        print('Myaah..Myaah...')

l = [Duck(),Dog(),Goat(),Cat()]
for obj in l:
    # obj.talk()
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()