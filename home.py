#Name: Pavneet 

from tkinter import *
# and import messagebox as mb from tkinter
from tkinter import messagebox as mb

# Create a GUI Window
root = Tk()
 
# set the size of the GUI Window
root.geometry("800x500")

# set minimum window size value
root.minsize(800, 500)
# set maximum window size value
root.maxsize(800, 500)

# set the title of the Window
root.title("Pavneets Geo Quiz")

# Define Image
bg = PhotoImage(file="image/Homewindow.new.png")

#font
f = ("Times bold", 14)

# Create a Label
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame - for background to stand out
my_frame = Frame(root)
my_frame.pack(pady=20)

#creating new pages (for quiz )

def nextPage():
    root.destroy()
    import quizlevel

Button(
    root, 
    text="click to start", 
    command=nextPage
    ).place(x=128, y=332)

root.mainloop()
