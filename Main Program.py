# Import the tools required for the program
from designwidgetgui import *
import tkinter
import csv
from tkinter import messagebox, simpledialog

# Create a base class to inherit the GUI class
class entryandsearch(CTProgramGUI):

# Create buttons to store inputted data entries and access search entries
    def __init__(gui):
        super().__init__()
        
        enter = tkinter.Button(gui.frame, text="Submit data", command=gui.register)
        enter.grid(row=2, column=0, sticky="news", padx=20, pady=10)
        search = tkinter.Button(gui.frame, text="Search data")
        search.grid(row=3, column=0, sticky="news", padx=20, pady=10)

# Create a file to store inputted data entries
    def register(gui):
        new_reg = [gui.name.get(), gui.date.get(), gui.gender.get(), gui.age.get(), gui.number.get(), gui.email.get(), gui.contacts.get()]
        with open("data_entries.csv", "a", newline='') as file:
            entry = csv.writer(file)
            entry.writerow(new_reg)
            messagebox.showinfo("Complete!", "Your information has been recorded!")
# Create a button to search inputted data entries

# Run the file 
app = entryandsearch()
app.run()