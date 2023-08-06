from tkinter import *

from quiz import Quiz

root = Quiz()


Button(
    root, 
    text="Previous Page", 
    command=prevPage
    ).place(x=228, y=432)

Button(
    root, 
    text="Next Page",
    command=nextPage
    ).place(x=128, y=332)

root.mainloop()
