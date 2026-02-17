import tkinter as tk
import os

root = tk.Tk()
root.title("Task Manager 💖")
root.geometry("400x450")

FILE_NAME = "tasks.txt"

# 🔹 Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                listbox.insert(tk.END, line.strip())

# 🔹 Save tasks to file
def save_tasks():
    with open(FILE_NAME, "w") as file:
        for i in range(listbox.size()):
            file.write(listbox.get(i) + "\n")

# 🔹 Add task with deadline
def add_task():
    task = entry_task.get()
    deadline = entry_deadline.get()

    if task != "" and deadline != "":
        full_task = task + " - " + deadline
        listbox.insert(tk.END, full_task)

        entry_task.delete(0, tk.END)
        entry_deadline.delete(0, tk.END)

        save_tasks()   # 💾 save after adding

# 🔹 Delete task
def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
        save_tasks()   # 💾 save after deleting

# 🔹 UI

tk.Label(root, text="Task").pack()
entry_task = tk.Entry(root, width=30)
entry_task.pack(pady=5)

tk.Label(root, text="Deadline").pack()
entry_deadline = tk.Entry(root, width=30)
entry_deadline.pack(pady=5)

tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=5)

listbox = tk.Listbox(root, width=40, height=12)
listbox.pack(pady=10)

# Load tasks at start
load_tasks()

root.mainloop()
