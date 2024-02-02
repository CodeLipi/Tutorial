# constructor overriding

class P:
    def __init__(self):
        print('parent constructor')
class C(P):
    def __init__(self):
        super().__init__()
        print('child constructor')

c = C()