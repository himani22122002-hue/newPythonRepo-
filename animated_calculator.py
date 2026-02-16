import tkinter as tk

root = tk.Tk()
root.title("Animated Calculator")
root.geometry("300x400")
root.configure(bg="#fce4ec")

operator = ""

# Press number
def press(num):
    entry.insert(tk.END, str(num))

# Store operator (SHOW it on screen)
def set_operator(op):
    global operator
    
    if entry.get() == "":
        return
    
    operator = op
    entry.insert(tk.END, op)   # ✅ show operator

#  Equal (NO eval)
def equal():
    global operator
    
    exp = entry.get()

    try:
        if operator in exp:
            parts = exp.split(operator)
            
            if len(parts) < 2:
                entry.delete(0, tk.END)
                entry.insert(0, "Oops!")
                return

            first = float(parts[0])
            second = float(parts[1])

            if operator == "+":
                result = first + second
            elif operator == "-":
                result = first - second
            elif operator == "*":
                result = first * second
            elif operator == "/":
                result = "Oops!" if second == 0 else first / second

            entry.delete(0, tk.END)
            entry.insert(0, result)

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Oops!")

#  Clear
def clear():
    global operator
    operator = ""
    entry.delete(0, tk.END)

# Animation Functions
def on_enter(e):
    e.widget['bg'] = "#f48fb1"

def on_leave(e):
    e.widget['bg'] = "#f8bbd0"

def on_click(e):
    e.widget.config(width=4, height=1)

def on_release(e):
    e.widget.config(width=5, height=2)

#  Display
entry = tk.Entry(root, width=15, font=("Comic Sans MS", 20), bd=5,
                 justify='right', bg="#fff0f5", fg="#d81b60")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Button style
btn_style = {
    "font": ("Comic Sans MS", 12),
    "bg": "#f8bbd0",
    "fg": "#880e4f",
    "width": 5,
    "height": 2
}

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3),
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        action = equal
    elif text == "C":
        action = clear
    elif text in ['+', '-', '*', '/']:
        action = lambda x=text: set_operator(x)
    else:
        action = lambda x=text: press(x)

    btn = tk.Button(root, text=text, command=action, **btn_style)
    btn.grid(row=row, column=col, padx=5, pady=5)

    # Animations
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.bind("<Button-1>", on_click)
    btn.bind("<ButtonRelease-1>", on_release)

# Run app
root.mainloop()
