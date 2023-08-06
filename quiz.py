from tkinter import Button, PhotoImage, Tk, constants


class Quiz(Tk):
    def __init__(self, image = None, home = False):
        super().__init__()
        self.geometry('800x500')
        self.title("Pavneet's Geography Quiz")
        self['bg'] = '#ffbf00'
        self.minsize(800, 500)
        self.maxsize(800, 500)
        if image:
            self.image = image
            self.bg = PhotoImage(file = self.image)
        if not home:
            Button(
                self,
                text = "Previous Page",
                command = self.prev_page
            ).pack(fill = constants.X, expand = constants.TRUE, side = constants.LEFT)
            Button(
                self,
                text = "Next Page",
                command = self.next_page
            ).pack(fill = constants.X, expand = constants.TRUE, side = constants.LEFT)


    def next_page(self):
        self.destroy()

    def prev_page(self):
        self.destroy()
