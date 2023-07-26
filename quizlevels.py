from tkinter import *

root = Tk()
root.geometry('800x500')
root.title('Pavneets Geo Quiz')
root['bg']='#ffbf00'
 
def nextPage():
    root.destroy()
    import startquiz

def prevPage():
    root.destroy()
    import home

Label(
    root,
    text="This is Second page",
    padx=20,
    pady=20,
    bg='#ffbf00',
).pack(expand=True, fill=BOTH)

Button(
    root, 
    text="Previous Page", 
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    root, 
    text="Next Page", 
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

root.mainloop()