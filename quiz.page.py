from tkinter import *

from quiz import Quiz

root = Quiz()

f = ("Times bold", 14)


Label(
    root,
    text="This is Third page",
    padx=20,
    pady=20,
    bg='#bfff00'
).pack(expand=True, fill=BOTH)

Button(
    root, 
    text="Previous Page", 
    font=f,
    command=prev_page
    ).pack(fill = X, expand = TRUE, side = LEFT)

Button(
    root,
    text="Next Page",
    command=next_page
    ).pack(fill=X, expand=TRUE, side=LEFT)

root.mainloop()
