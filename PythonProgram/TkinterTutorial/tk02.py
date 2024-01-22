# Frame widget which may contain other widgets and can have a 3D border.

from tkinter import *

root = Tk()
root.title('Frame widget')

frame = Frame(root)
frame.pack()  # frame is packed with root window

button = Button(frame, text='Click Me!')
button.pack()  # button is packed with frame window

root.mainloop()