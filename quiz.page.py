from tkinter import *

root = Tk()
root.geometry('800x500')
root.title('Pavneets Geo Quiz')
root['bg']='#ffbf00'

f = ("Times bold", 14)

def nextPage():
    root.destroy()
    import home

def prevPage():
    root.destroy()
    import quizlevels

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
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    root, 
    text="Next Page",
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

root.mainloop()