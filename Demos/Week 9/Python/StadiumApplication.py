import tkinter as tk
from Model import Model
from View import View
from Controller import Controller

class StadiumApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the title
        self.title('Stadium')

        # Create a model
        model = Model()

        # Create a view and place it on the root window
        view = View(self)
        view.grid(row=0, column=0)

        # Create a controller
        controller = Controller(model, view)

        # Set the controller to the view
        view.set_controller(controller)

if __name__ == '__main__':
    app = StadiumApplication()
    app.mainloop()