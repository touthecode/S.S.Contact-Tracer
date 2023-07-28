import tkinter
from tkinter import ttk

# Make a class that will make the GUI accessible to the main program 
class CTProgramGUI:
    # Make the base app graphics and dimensions
    def __init__(gui):
        gui.window = tkinter.Tk()
        gui.window.title("Covid 19 Contact Tracing App")

        gui.frame = tkinter.Frame(gui.window)
        gui.frame.pack()

        # Make inputs into retrievable string variables
        gui.name = tk.StringVar()
        gui.date = tk.StringVar()
        gui.gender = tk.StringVar()
        gui.age = tk.StringVar()
        gui.number = tk.StringVar()
        gui.email = tk.StringVar()
        gui.contacts = tk.StringVar()

        # Create and design widgets to input data
        user_input_frame = tkinter.LabelFrame(gui.frame, text="General User Information")
        user_input_frame.grid(row=0, column=0, padx=20, pady=20)
        
        # Rest of your widget creation code...
        full_name_label = tkinter.Label(user_input_frame, text="Full Name: ")
        full_name_label.grid(row= 0, column= 0)
        date_label = tkinter.Label(user_input_frame, text="Date: ")
        date_label.grid(row= 0, column= 1)

        full_name_input = tkinter.Entry(user_input_frame, variable=gui.name)
        full_name_input.grid(row= 1, column= 0)
        date_input = tkinter.Entry(user_input_frame, variable=gui.date)
        date_input.grid(row= 1, column= 1)

        gender_input = tkinter.Label(user_input_frame, text="Gender: ")
        gender_input.grid(row= 0, column= 2)
        gender_input = ttk.Combobox(user_input_frame, values=["Male", "Female", "Prefer not to say"], variable=gui.gender)
        gender_input.grid(row= 1, column= 2)

        age_label = tkinter.Label(user_input_frame, text="Age")
        age_label.grid(row=2, column=0)
        age_spinbox = tkinter.Spinbox(user_input_frame, from_=1, to=120, variable= gui.age)
        age_spinbox.grid(row=3, column=0)

        contact_num_label = tkinter.Label(user_input_frame, text="Contact Number: ")
        contact_num_label.grid(row= 2, column= 1)
        contact_num_input = tkinter.Entry(user_input_frame, variable=gui.number)
        contact_num_input.grid(row= 3, column= 1)

        email_info_label = tkinter.Label(user_input_frame, text="Email Info: ")
        email_info_label.grid(row= 2, column= 2)
        email_info_input = tkinter.Entry(user_input_frame, variable=gui.email)
        email_info_input.grid(row= 3, column= 2)

        last_contact_label = tkinter.Label(user_input_frame, text="Last Contacts: (F.N. L.N , +)")
        last_contact_label.grid(row= 4, column= 1)
        last_contact_input = tkinter.Entry(user_input_frame, variable=gui.contacts)
        last_contact_input.grid(row= 5, column= 1)


        for widget in user_input_frame.winfo_children():
            widget.grid_configure(padx=20, pady=10)

    # Make a function to run the whole thing
    def run(gui):
        gui.frame.mainloop()




