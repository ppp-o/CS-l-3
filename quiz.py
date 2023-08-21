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
    ).place(x=228, y=332)

Button(
    root, 
    text="home",
    command=nextPage
    ).place(x=328, y=432)

root.mainloop()