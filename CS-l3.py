#Name: Pavneet 

from tkinter import *
# and import messagebox as mb from tkinter
from tkinter import messagebox as mb


# Create a GUI Window
root = Tk()
 
# set the size of the GUI Window
root.geometry("800x500")

# set minimum window size value
root.minsize(800, 500)
 
# set maximum window size value
root.maxsize(800, 500)
# set the title of the Window
root.title("Pavneet's Geo Quiz")

# Define Image
bg = PhotoImage(file="image/Homewindow.new.png")

# Create a Label
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame - for background to stand out
my_frame = Frame(root)
my_frame.pack(pady=20)

# making button function by allowing it to take you into a new window 
def openwindow():
    return True

btn = Button(root, text="click to start", command=openwindow)
btn.pack(padx=20, pady=20)



root.mainloop()





