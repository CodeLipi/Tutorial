# tk tutorial (introduction)

from tkinter import *


# root (parent window)
root = Tk()

# set title
root.title('Test')
print('Welcome to tk')

# setting icon
# root.iconbitmap('/Tutorial/TkinterTutorial/icon.ico') 
root.iconbitmap('icon.ico') 

# set size (setting fixed sized)
# we can not set full screen size
# root.maxsize(width=300,height=600)
# root.minsize(width=300,height=600)

# 2nd way to set size
# here we can to full size
root.geometry('600x300')

# run continuously
root.mainloop()
