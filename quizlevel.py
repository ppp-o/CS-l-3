from tkinter import *
# and import messagebox as mb from tkinter
from tkinter import messagebox as mb
import tkinter as tk

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

# Define Image
bg = PhotoImage(file="image/quizlevel.png")

# Create a Label
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

# creating function to check for vaild login information 
def check_user_info():
    name = name_entry.get()
    age = age_entry.get()

    if not name or not name.isalpha():
        name_error_label.config(text="No numbers in name ")
    else:
        name_error_label.config(text="")

    if not age.isdigit() or int(age) < 7 or int(age) > 12:
        age_error_label.config(text="7-12 only ")
    else:
        age_error_label.config(text="")


#labels for end user name and age 
name_label = tk.Label(root, text="Name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

name_error_label = tk.Label(root, text="", fg="red")
name_error_label.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()

age_entry = tk.Entry(root)
age_entry.pack()

age_error_label = tk.Label(root, text="", fg="red")
age_error_label.pack()

startquiz_button = tk.Button(root, text="Start quiz", command=check_user_info)
startquiz_button.pack()


def nextPage():
    root.destroy()
    import quiz

def prevPage():
    root.destroy()
    import home

Button(
    root, 
    text="Home", 
    command=prevPage
    ).place(x=150, y=400)

"""Button(
    root, 
    text="Start quiz", 
    command=nextPage
    ).place(x=550, y=400)"""

def Close():
    root.destroy()
  
# Button for quiting quiz
exit_button = Button(root, text="Quit", command=Close)
exit_button.place(x=550, y=400)

root.mainloop()