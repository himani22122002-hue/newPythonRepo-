import tkinter as tk

root = tk.Tk()
root.title("Cute Calculator 💖")
root.geometry("300x400")
root.configure(bg="#fce4ec")  # light pink background

expression = ""

def press(num):
    global expression
    expression += str(num)
    entry.delete(0, tk.END)
    entry.insert(0, expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, result)
        expression = result
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Oops!")
        expression = ""

def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

# Display
entry = tk.Entry(root, width=15, font=("Comic Sans MS", 20), bd=5, justify='right',
                 bg="#fff0f5", fg="#d81b60")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Button style
btn_style = {
    "font": ("Comic Sans MS", 12),
    "bg": "#f8bbd0",   # light pink
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

for (text, row, col) in buttons:
    if text == "=":
        action = equal
    elif text == "C":
        action = clear
    else:
        action = lambda x=text: press(x)

    tk.Button(root, text=text, command=action, **btn_style)\
        .grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
