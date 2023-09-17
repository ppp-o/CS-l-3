from tkinter import *
# and import messagebox as mb from tkinter
from tkinter import messagebox as mb
import json

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

# Define bg Image
bg = PhotoImage(file="image/quizbg.png")
# Create a Label for bg
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

# get data from json file
with open('data.json') as f:
    data = json.load(f)

# function for home button 
def nextPage():
    root.destroy()
    import home
# button to take end user back to home
Button(
    root, 
    text="home",
    command=nextPage
    ).place(x=150, y=400)

# function for quiting quiz
def Close():
    root.destroy()
# Button for quiting quiz
exit_button = Button(root, text="Quit", command=Close)
exit_button.place(x=550, y=400)

#class for the different components of this quiz 
class Quiz:
    def __init__(self):
        # to set question number to 0 at start of quiz
        self.q_no=0
        self.display_question()
        # opt_selected holds an integer value which is used for selected option in a question
        self.opt_selected=IntVar()
        # displayings radio button for the current question and used to display options for the current question
        self.opts=self.radio_buttons()
        # display options for the current question
        self.display_options()
        # displays the button for next 
        self.buttons()
        # no of questions
        self.data_size=len(question)
        # keep a counter of correct answers
        self.correct=0
 
    # This function displays the result, It records the number of correct and wrong answers,
    # which will then be displayed at the end in a message Box
    def display_result(self):
        # calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
         
        # calculting the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"

        # button to take end user back to home page
        def prevPage():
            root.destroy()
            import home

        Button(
            root, 
            text="Home", 
            command=prevPage
            ).place(x=150, y=400)
         
        # message box to display the quiz results to the end user
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")
        mb.geometry("400x200")


    #checking the answer after end user clicks Next button
    def check_ans(self, q_no):
        # checks if selected option/answer is correct
        if self.opt_selected.get() == answer[q_no]:
            # if the option/answer is correct it returns as true
            return True
 
    # This function checks the answer of the current question by calling the check_ans and question no,
    # if the question is correct it increases the count by 1 or if the question is incorrect there is no increase or decrease in the count
    # and then there will also be an increase in the question number (no) by 1.
    # If its the last question then it calls display result to show the message box,
    # otherwise next question will be showen
    def next_btn(self):
        # Checking if the answer is correct
        if self.check_ans(self.q_no): 
            # if the answer is correct it increasses the correct by 1
            self.correct += 1

        # Moves to next Question by increassing the q_no counter
        self.q_no += 1
        # checks if the q_no size is equal to the data size
        if self.q_no==self.data_size:
             
            # if q_no is equal to data size then the score/results are displayed 
            self.display_result()
             
            # destroys GUI
            root.destroy()
        else:
            # shows next question
            self.display_question()
            self.display_options()
 
    # This shows the properties of the next button on the quiz/
    # The next button moves end user to next question on quiz
    def buttons(self):
        next_button = Button(root, text="Next",command=self.next_btn,
        width=10,bg="green",fg="white",font=("ariel",16,"bold"))
        next_button.place(x=350,y=380)
 
    # This function deselect the radio button on the screen.
    # Then it is used to display the options available for the current question,
    # which is obtained/displayed through the question number and Updates
    def display_options(self):
        val=0
        # deselecting the options
        self.opt_selected.set(0)
        # looping over the options to be displayed for the text of the radio buttons.
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1
 
    # This shows the current question on the screen
    def display_question(self):
        # setting the question properties
        q_no = Label(root, text=question[self.q_no], width=60,
        font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
        q_no.place(x=70, y=100)
 
    # This function displays/positions the 4 radio buttons
    def radio_buttons(self): 
        # initialize the list with an empty list of options
        q_list = []
        # position of the first option
        y_pos = 150
        # adding options to the list
        while len(q_list) < 4:
            # radio buttons properties
            radio_btn = Radiobutton(root,text=" ",variable=self.opt_selected,
            value = len(q_list)+1,font = ("ariel",14))
            # adding the button to the list
            q_list.append(radio_btn)
            # placing the 4 radio button
            radio_btn.place(x = 100, y = y_pos)
            # incressing the y-axis position by 50
            y_pos += 50
        # return the radio buttons
        return q_list
 
# question, options, and answer
question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])
 
# to run the quiz
quiz = Quiz()
root.mainloop()