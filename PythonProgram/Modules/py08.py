# module 3

def f1():
    if __name__ == '__main__':
        print("Directly execution")
        print("__name__ : ", __name__)
    else:
        print("Indirectly execution")
        print("__name__ : ", __name__)

f1()