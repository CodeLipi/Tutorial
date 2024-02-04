# handling csv file
# writing in csv file
import csv

with open('emp.csv', 'w', newline='') as f:   # if we not add newline attr then its added a extra newline after every input data
    w = csv.writer(f)      # returns csv writer object pointing to f
    w.writerow(['Employee_No','Employee_Name','Employee_Salary','Empoloyee_Address'])
    n = int(input('Enter no of employee : '))
    for i in range(n):
        eno = int(input('Enter employee no : '))
        ename = input('Enter employee name : ')
        esal = float(input('Enter employee salary : '))
        eaddr = input('Enter employee address (only city): ')
        w.writerow([eno,ename,esal,eaddr])

print('Total employees data written to csv file .....')
