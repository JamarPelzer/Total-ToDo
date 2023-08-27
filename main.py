import tkinter as tk
from tkinter import font, Entry, Button, Listbox


def add():
    task_input = task_entry.get()
    processed_text = "-" + " " + task_input.strip()
    if processed_text:
        task_list.insert(tk.END, processed_text)
        task_entry.delete(0, tk.END)


def delete():
    clear_task = task_list.curselection()
    for index in clear_task:
        task_list.delete(index)


# Create the application Interface
gui = tk.Tk()
gui.title("TO-DO List")
gui.geometry("650x450")
gui.resizable(False, False)
gui.configure(bg="light gray")

# Create a label that shows the title of our app
label_font = font.Font(slant="italic", size=30, family="courier")
label_1 = tk.Label(gui, compound="center", text="THE TO-DO APP", font=label_font, bg="orange", height=2, width=100,
                   fg="black")
label_1.pack()

# create a label "Add Task"
sub_font = font.Font(slant="italic", size=20, family="courier")
add_task = tk.Label(gui, compound="center", text="Add Task", font=sub_font, bg="orange", height=2, width=15, fg="black")
add_task.place(x=15, y=80)

# Create a label"Task"
task = tk.Label(gui, compound="center", text="Task", font=sub_font, bg="orange", height=2, width=15, fg="black")
task.place(x=400, y=80)

# Create an add button
add_button = Button(gui, font=sub_font, text="Add", width=10, height=2, bg="#0052cc", fg="black", command=add)
add_button.place(x=15, y=230)

# Create a delete button
delete_button = Button(gui, font=sub_font, text="Delete", width=10, height=2, bg="orange", fg="black", command=delete)
delete_button.place(x=15, y=300)

# Create entry Field
task_entry = Entry(gui, width=15, highlightthickness=2, bg="white", fg="black", font=sub_font)
task_entry.place(x=15, y=150)

# Create a listbox where your task items are placed
task_font = font.Font(slant="italic", size=18, family="courier")
task_list = Listbox(gui, bg="white", width=30, height=15, fg="black", font=task_font)
task_list.place(x=300, y=150)

gui.mainloop()
