# first program in gui using tkinter


from tkinter import *
# from tkinter.ttk import *

root = Tk()    # root window of the whole program
root.title('First_Program')

label = Label(root,
    text = 'Welcome in GUI World!',
    width = 40,
    height = 20
)
label.pack()

root.mainloop()
