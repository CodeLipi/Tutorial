class P:
    def __init__(self):
        self.x = 10

class C(P):
    def __init__(self):
        # self.x = 20
        # super().__init__()
        # print(self.__dict__)  # {'x': 10}

        super().__init__()
        self.x = 20
        print(self.__dict__)   # {'x': 20}

        # print(super().x)    # AttributeError: 'super' object has no attribute 'x'
        # we cant access instance var using super() methed, it is possible only with self keyword.
c = C()
