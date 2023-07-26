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

# Create a Label
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame - for background to stand out
my_frame = Frame(root)
my_frame.pack(pady=20)

btn = Button(root, text="click to start") #, command=openwindow)
btn.place(x=128, y=332)

#creating new pages 

def nextPage():
    root.destroy()
    import quizlevels

Label(
    root,
    text="Quiz levels",
    padx=20,
    pady=20,
    bg='#5d8a82',
).pack(expand=True, fill=BOTH)

Button(
    root, 
    text="click to start", 
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

root.mainloop()
