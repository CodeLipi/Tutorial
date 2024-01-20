# grid system

from tkinter import *

root = Tk()
root.title('Grid System')

label_1 = Label(root,text='This is label 1')
label_2 = Label(root,text='This is label 2')

label_1.grid(row=0,column=0)
label_2.grid(row=1,column=1)

root.after(100)
root.mainloop()