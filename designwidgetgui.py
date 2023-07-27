# Import the tools required for the program
import tkinter
from tkinter import ttk

# Make a class that will make the GUI accessible to the main program 
class CTProgramGUI:

# Make the base app graphics and dimensions
    def __init__(gui):
        gui.window = tkinter.Tk()
        gui.window.title("Covid 19 Contact Tracing App")

        frame = tkinter.Frame(gui.window)
        frame.pack()

        user_input_frame =tkinter.LabelFrame(frame, text="General User Information")
        user_input_frame.grid(row= 0, column= 0, padx= 20, pady =20)
        

        full_name_label = tkinter.Label(user_input_frame, text="Full Name: ")
        full_name_label.grid(row= 0, column= 0)
        date_label = tkinter.Label(user_input_frame, text="Date: ")
        date_label.grid(row= 0, column= 1)

        full_name_input = tkinter.Entry(user_input_frame)
        full_name_input.grid(row= 1, column= 0)
        date_input = tkinter.Entry(user_input_frame)
        date_input.grid(row= 1, column= 1)

        gender_input = tkinter.Label(user_input_frame, text="Gender: ")
        gender_input.grid(row= 0, column= 2)
        gender_input = ttk.Combobox(user_input_frame, values=["Male", "Female", "Prefer not to say"])
        gender_input.grid(row= 1, column= 2)

        age_label = tkinter.Label(user_input_frame, text="Age")
        age_label.grid(row=2, column=0)
        age_spinbox = tkinter.Spinbox(user_input_frame, from_=1, to=120)
        age_spinbox.grid(row=3, column=0)

        contact_num_label = tkinter.Label(user_input_frame, text="Contact Number: ")
        contact_num_label.grid(row= 2, column= 1)
        contact_num_input = tkinter.Entry(user_input_frame)
        contact_num_input.grid(row= 3, column= 1)

        email_info_label = tkinter.Label(user_input_frame, text="Email Info: ")
        email_info_label.grid(row= 2, column= 2)
        email_info_input = tkinter.Entry(user_input_frame)
        email_info_input.grid(row= 3, column= 2)

        for widget in user_input_frame.winfo_children():
            widget.grid_configure(padx=20, pady=10)


        gui.window.mainloop()





# Make inputs into retrievable string variables
# Create and design widgets to input data
# Make a function to run the whole thing


app = CTProgramGUI()
app.run
