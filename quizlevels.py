from tkinter import *

from quiz import Quiz

root = Quiz("image/quizlevel.png")



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
