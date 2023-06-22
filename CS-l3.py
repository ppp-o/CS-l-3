#Name: Pavneet - testing 

from tkinter import *
# and import messagebox as mb from tkinter
from tkinter import messagebox as mb


# Create a GUI Window
root = Tk()
 
# set the size of the GUI Window
root.geometry("800x450")
 
# set the title of the Window
root.title("Pavneet's Geo Quiz")
 
bg = PhotoImage(file= "homewindow.png")
Label = Label(root, image = bg)
Label.place (x = 0, y = 0)

root.mainloop()




