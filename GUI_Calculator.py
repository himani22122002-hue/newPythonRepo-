import tkinter as tk

# Create window
root = tk.Tk()
root.title("Simple Calculator")

# Variable to store input
expression = ""

# Function to show input on screen
def press(num):
    global expression
    expression = expression + str(num)
    entry.delete(0, tk.END)
    entry.insert(0, expression)

# Function to calculate result
def equal():
    global expression
    try:
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, result)
        expression = result
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        expression = ""

# Function to clear screen
def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

# Input box
entry = tk.Entry(root, width=18, font=("Arial", 18), bd=5, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Buttons
tk.Button(root, text="1", width=5, height=2, command=lambda: press(1)).grid(row=1, column=0)
tk.Button(root, text="2", width=5, height=2, command=lambda: press(2)).grid(row=1, column=1)
tk.Button(root, text="3", width=5, height=2, command=lambda: press(3)).grid(row=1, column=2)
tk.Button(root, text="+", width=5, height=2, command=lambda: press('+')).grid(row=1, column=3)

tk.Button(root, text="4", width=5, height=2, command=lambda: press(4)).grid(row=2, column=0)
tk.Button(root, text="5", width=5, height=2, command=lambda: press(5)).grid(row=2, column=1)
tk.Button(root, text="6", width=5, height=2, command=lambda: press(6)).grid(row=2, column=2)
tk.Button(root, text="-", width=5, height=2, command=lambda: press('-')).grid(row=2, column=3)

tk.Button(root, text="7", width=5, height=2, command=lambda: press(7)).grid(row=3, column=0)
tk.Button(root, text="8", width=5, height=2, command=lambda: press(8)).grid(row=3, column=1)
tk.Button(root, text="9", width=5, height=2, command=lambda: press(9)).grid(row=3, column=2)
tk.Button(root, text="*", width=5, height=2, command=lambda: press('*')).grid(row=3, column=3)

tk.Button(root, text="0", width=5, height=2, command=lambda: press(0)).grid(row=4, column=0)
tk.Button(root, text="C", width=5, height=2, command=clear).grid(row=4, column=1)
tk.Button(root, text="=", width=5, height=2, command=equal).grid(row=4, column=2)
tk.Button(root, text="/", width=5, height=2, command=lambda: press('/')).grid(row=4, column=3)

# Run app
root.mainloop()
