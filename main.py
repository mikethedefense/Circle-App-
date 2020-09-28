import logging
from math import pi, sqrt
from tkinter import *
from tkinter import messagebox

__version__ = "1.00"

logging.basicConfig(level = logging.DEBUG) 

def circle_area(radius = None, area = None):
    """
    Logic for circle area
    """
    if radius is not None:
        area = round(pi * (radius ** 2), 3)
        return area
    else:
        radius = round(sqrt(area/pi), 3)
        return radius

# Main script
root = Tk()
root.title("Circle Area Calculator")
root.geometry("300x300")

# Variables
answer = 0
history = []
history_labels = []
history_displayed = False

# Init and grid the Entries
e = Entry(root, width = 10, borderwidth = 5)
e_2 = Entry(root, width = 10, borderwidth = 5)
e.grid(row = 0, column = 1)
e_2.grid(row = 1, column = 1)
e.get()
e_2.get()

# Init and Grid Labels
Radius_Label = Label(root, text = "Radius:", fg = "Blue")
Area_Label = Label(root, text = "Area:", fg = "Green")
Radius_Label.grid(row = 0, column = 0)
Area_Label.grid(row = 1, column = 0)

def get_value():
    """ 
    Function that will process the input and give an answer in another input box
    """
    global history 
    global answer
    
    if e.get() != "" and e_2.get() == "":
        try:
            answer  = circle_area(radius = int(e.get()))
            answer = str(answer)
            logging.debug(answer)
            e_2.insert(1, answer)
            history.append(answer)
            Answer_Button["state"] = DISABLED
        except ValueError as f:
            messagebox.showerror("Error", f)
            logging.debug(f)
            e.delete(0, END)
        
    elif e_2.get() != "" and e.get() == "":
        try:
            answer = circle_area(area = int(e_2.get()))
            logging.debug(answer)
            answer = str(answer)
            e.insert(0, answer)
            history.append(answer)
            Answer_Button["state"] = DISABLED
        except ValueError as f:
            messagebox.showerror("Error", f)
            logging.debug(f)
            e_2.delete(0, END)
    else:
        messagebox.showerror("Error", "Only one Input allowed") 

def delete():
    """
    Function that deletes the values in the entry box
    """
    e.delete(0, END)
    e_2.delete(0, END)
    Answer_Button["state"] = NORMAL
    answer = 0 

def show_history():
    """
    Function that will list all the history of the answers and show/hide
    """
    global history_displayed
    global history_labels
    
    if history_displayed:
        for label in history_labels:
            label.grid_forget()
    
    else:
        for count,num in enumerate(history):
            Label_List = Label(root, text = num)
            Label_List.grid(row = count + 5, column = 0)
            history_labels.append(Label_List) 
            
    history_displayed = not history_displayed

# Grid and Inits for Buttons
Answer_Button = Button(root, text = "Click for answer", command = get_value)
Delete_Button = Button(root, text = "Clear Entry", command = delete)
Exit_Button = Button(root, text = "Exit", command = root.quit)
History_Button = Button(root, text = "Show History", command = show_history)
Answer_Button.grid(row = 2, column = 2)
Delete_Button.grid(row = 2 , column = 1)
Exit_Button.grid(row = 3, column = 2)
History_Button.grid(row = 4, column = 0)

root.mainloop()
