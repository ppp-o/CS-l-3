from tkinter import *

root = Tk()
root.title('Pavneets Geo Quiz')

# set the size of the GUI Window
root.geometry("800x500")

# set minimum window size value
root.minsize(800, 500)
# set maximum window size value
root.maxsize(800, 500)
 
#font
f = ("Times bold", 14)

def nextPage():
    root.destroy()
    import home

def prevPage():
    root.destroy()
    import quizlevel

Button(
    root, 
    text="perv", 
    command=prevPage
    ).place(x=150, y=400)

Button(
    root, 
    text="home",
    command=nextPage
    ).place(x=550, y=400)

root.mainloop()