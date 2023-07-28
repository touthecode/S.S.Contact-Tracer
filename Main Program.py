# Import the tools required for the program
from designwidgetgui import *
import tkinter
import csv
from tkinter import ttk

# Create a base class to inherit the GUI class
class entryandsearch(CTProgramGUI):

# Create buttons to store inputted data entries and access search entries
    def __init__(gui):
        super().__init__()
        
        enter = tkinter.Button(gui.frame, text="Submit data")
        enter.grid(row=2, column=0, sticky="news", padx=20, pady=10)


# Create a file to store inputted data entries
# Create a button to search inputted data entries

# Run the file 
app = entryandsearch()
app.run()