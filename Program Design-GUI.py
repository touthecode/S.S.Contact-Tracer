# Import the tools required for the program
import tkinter
import csv
from tkinter import ttk

# Make a class that will make the GUI accessible to the main program 
class CTProgramGUI:

# Make the base app graphics and dimensions
    def __init__(gui):
        gui.window = tkinter.Tk()
        gui.window.title("Covid 19 Contact Tracing App")

        frame = tkinter.Frame(gui.window)
        frame.pack()
        gui.window.mainloop()


# Make inputs into retrievable string variables
# Create and design widgets to input data
# Make a function to run the whole thing


app = CTProgramGUI()
app.run
