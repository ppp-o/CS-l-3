#Name: Pavneet - testing 

from tkinter import *
# and import messagebox as mb from tkinter
from tkinter import messagebox as mb


# Create a GUI Window
root = Tk()
 
# set the size of the GUI Window
root.geometry("900x500")
 
# set the title of the Window
root.title("Pavneet's Geo Quiz")

# Define Image
bg = PhotoImage(file= "Homewindow.png")
#Label = Label(root, image = bg)
#Label.place (x = 0, y = 0)

# Create a Label
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame - for background to stand out
my_frame = Frame(root)
my_frame.pack(pady=20)

root.mainloop()




