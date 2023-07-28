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
        gui.inquiry = tkinter.Frame(gui.window)
        gui.inquiry.pack()

        gui.search = tkinter.StringVar()

        enter = tkinter.Button(gui.frame, text="Submit data", command=gui.register)
        enter.grid(row=2, column=0, sticky="news", padx=20, pady=10)

        search = tkinter.Button(gui.frame, text="Search data", command=gui.find)
        search.grid(row=4, column=0, sticky="news", padx=20, pady=10)

        user_entry_frame = tkinter.LabelFrame(gui.frame, text="Search Entries Here: ")
        user_entry_frame.grid(row=5, column=0, padx=20, pady=20)

        search_inquiry = tkinter.Label(user_entry_frame, text="Search a name: LN")
        search_inquiry.grid(row= 5, column= 1)

        search_inquiry = tkinter.Entry(user_entry_frame, text="Search a name: LN, FN", textvar=gui.search)
        search_inquiry.grid(row= 6, column= 1)

        for widget in user_entry_frame.winfo_children():
            widget.grid_configure(padx=20, pady=10)

# Create a file to store inputted data entries
    def register(gui):
        new_reg = [gui.name.get(), gui.date.get(), gui.gender.get(), gui.age.get(), gui.number.get(), gui.email.get(), gui.contacts.get()]
        with open("data_entries.csv", "a", newline='') as file:
            entry = csv.writer(file)
            entry.writerow(new_reg)
            messagebox.showinfo("Complete!", "Your information has been recorded!")

# Create a function to search inputted data entries
    def find(gui):
        wanted_contact = gui.search.get()

        with open("data_entries.csv", 'r') as text:
            csv_reader = csv.reader(text)
            for row in csv_reader:
                if wanted_contact in row:
                    messagebox.showinfo("Found it!", f"Entry found: {row}")
                    return
        messagebox.showinfo("Sorry D:", "Can't find it")

# Run the file 
app = entryandsearch()
app.run()