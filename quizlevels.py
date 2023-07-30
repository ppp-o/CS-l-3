from tkinter import *

root = Tk()
root.title('Pavneets Geo Quiz')

# set the size of the GUI Window
root.geometry("800x500")

# set minimum window size value
root.minsize(800, 500)
# set maximum window size value
root.maxsize(800, 500)
 
# Define Image
bg = PhotoImage(file="image/quizlevel.png")

def nextPage():
    root.destroy()
    import startquiz

def prevPage():
    root.destroy()
    import home


Button(
    root, 
    text="Home", 
    command=prevPage
    ).place(x=228, y=432)

Button(
    root, 
    text="Next Page", 
    command=nextPage
    ).place(x=128, y=332)

Button(
    root, 
    text="easy quiz"
    "command= have new window that opens"
).place(x=328, y=532)

Button(
    root, 
    text="quiz"
    "command= have new window that opens"
).place(x=428, y=632)

Button(
    root, 
    text="hard quiz"
    "command= have new window that opens"
).place(x=528, y=732)

root.mainloop()