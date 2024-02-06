# combo-box

from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('600x400')

combo_box = ttk.Combobox(root, width=10)

combo_box['values'] = ('Jan',
                       'Feb',
                       'Mar',
                       'Apr',
                       'May',
                       'Jun',
                       'Jul',
                       'Aug',
                       'Sep',
                       'Oct',
                       'Nov',
                       'Dec')
combo_box.place(x=10, y=5)

root.mainloop()
