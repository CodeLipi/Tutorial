try:
    print('statement 1')
    # print('statement 2')
    print(10/0)
    print('statement 3')
    try:
        print('statement 4')
        print('statement 5')
        print('statement 6')
    except:
        print('statement 7')
    finally:
        print('statement 8')
    print('statement 9')
except:
    print('statement 10')
finally:
    print('statement 11')
print('statement 12')