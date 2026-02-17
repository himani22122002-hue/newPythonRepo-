import tkinter as tk

root = tk.Tk()
root.title("Task Manager")
root.geometry("400x400")

tasks = []

# Add task
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

# Delete task
def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

# Entry box
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Buttons
tk.Button(root, text="Add Task", command=add_task).pack()
tk.Button(root, text="Delete Task", command=delete_task).pack()

# List to show tasks
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

root.mainloop()