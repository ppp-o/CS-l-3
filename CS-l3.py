#Name: Pavneet 

from tkinter import *
# and import messagebox as mb from tkinter
from tkinter import messagebox as mb


# Create a GUI Window
root = Tk()
 
# set the size of the GUI Window
root.geometry("800x500")
 
# set the title of the Window
root.title("Pavneet's Geo Quiz")

# Define Image
bg = PhotoImage(file="image/Homewindow.new.png")

# Create a Label
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame - for background to stand out
my_frame = Frame(root)
my_frame.pack(pady=20)

# Add some buttons and now put buttons inside the frame just added
my_button1 = Button(my_frame, text="click to start")
my_button1.grid(row=0, column=0, padx=20)


root.mainloop()





