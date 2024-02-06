# label

from tkinter import *

root = Tk()
root.geometry('600x400')

label = Label(root, 
              text='UserName', 
              bg='blue', 
              fg='white',
              height=10,
              width=10
              )

label.pack()  # fix this on the root
# label.grid()  # fix this on the root using row and colmn
# label.grid(row=5,column=3)  # fix this on the root using row and colmn
# label.place()  # place using 2d space
# label.place(x=10,y=20)

root.mainloop()