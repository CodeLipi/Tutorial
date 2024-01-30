class Employee:
    def __init__(self,id,name,salary,address):
        self.name = name
        self.id = id
        self.salary = salary
        self.address = address

        # vertical are instance variable
    def display(self):
        print(self.name, self.id, self.salary, self.address)