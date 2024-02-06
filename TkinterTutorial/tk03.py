# entry box and button

from tkinter import *

root = Tk()
root.geometry('600x400')


def func():
    x = input_value.get()
    label2.config(text=x)


# output label
label2 = Label(root,
               text='Nothing',
               font='Calibri 10 bold'
               )
label2.place(x=25, y=65)

# input label
label = Label(root,
              text='UserName',
              font='Calibri 10 bold'
              )
label.place(x=10, y=10)

# entry box for input
input_value = StringVar()
entry = Entry(root,
              textvariable=input_value
              )
entry.place(x=80, y=10)

# button
btn = Button(root,
             text='Submit',
             command=func
             )
btn.place(x=25, y=30)

root.mainloop()
