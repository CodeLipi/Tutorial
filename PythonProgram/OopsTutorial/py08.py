class Test: 
    def __init__(self):
        print('Constructor execution...  ',id(self))

t = Test()    # constructor internally executed
t.__init__()   # constructor externally executed
t.__init__()
t.__init__()
t.__init__()
t.__init__()

# only once object is created.