#Name: Pavneet 

from tkinter import *
# and import messagebox as mb from tkinter
from tkinter import messagebox as mb
import tkinter as tk

# Create a GUI Window
root = Tk()
 
# set the size of the GUI Window
root.geometry("800x500")

# set minimum window size value
root.minsize(800, 500)
# set maximum window size value
root.maxsize(800, 500)

# set the title of the Window
root.title("Pavneets Geo Quiz")

# Define Image
bg = PhotoImage(file="image/Homewindow.png")

#font
f = ("Times bold", 14)

# Create a Label
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame - for background to stand out
my_frame = Frame(root)
my_frame.pack(pady=20)

# creating function to check for vaild login information 
def check_user_info_and_nextPage():
    name = name_entry.get()
    age = age_entry.get()

    if not name or not name.isalpha():
        name_error_label.config(text="letters only")
    else:
        name_error_label.config(text="")

    if not age.isdigit() or int(age) < 7 or int(age) > 12:
        age_error_label.config(text="7-12 only")
    else:
        age_error_label.config(text="")
    if name and name.isalpha() and age.isdigit() and 7 <= int(age) <= 12:
        root.destroy()
        import quiz

#labels for end user name and age 
name_label = tk.Label(root, text="Name:")
name_label.place(x = 100, y = 250)

name_entry = tk.Entry(root)
name_entry.place(x = 150, y = 250)

name_error_label = tk.Label(root, text="", fg="red")
name_error_label.place(x = 335, y = 250)

age_label = tk.Label(root, text="Age:")
age_label.place(x = 100, y = 300)

age_entry = tk.Entry(root)
age_entry.place(x = 150, y = 300)

age_error_label = tk.Label(root, text="", fg="red")
age_error_label.place(x = 335, y = 300)

#button to start quiz
startquiz_button = tk.Button(root, text="Start quiz", command=check_user_info_and_nextPage)
startquiz_button.place(x = 200, y = 350)


root.mainloop()
