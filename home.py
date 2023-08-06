# Name: Pavneet

from tkinter import *
# and import messagebox as mb from tkinter
from tkinter import messagebox as mb

from quiz import Quiz

root = Quiz("image/Homewindow.new.png", True)

# Create a Label
my_label = Label(root, image = root.bg)
my_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# Create a frame - for background to stand out
my_frame = Frame(root)
my_frame.pack(pady = 20)


# creating new pages



Button(
    root,
    text = "click to start",
    command = next_page
).place(x = 128, y = 332)

root.mainloop()
