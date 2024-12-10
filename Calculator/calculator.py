# Importing Tkinter library
from tkinter import Tk, Label, Button, Entry

# Function to perform the calculations
def calculate():
    try:
        # Get the input expression
        expression = entry.get()
        # Evaluate the expression
        result = eval(expression)
        # Display the result in the label
        result_label.config(text=f"Result: {result}")
    except Exception as e:
        # Display error message
        result_label.config(text="Error: Invalid Input")

# Create the main window
root = Tk()
root.title("Simple Calculator")

# Entry widget for the input expression
entry = Entry(root, width=20, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons for numbers and operators
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    def on_click(b=button):  # Closure to handle button clicks
        if b == "=":
            calculate()
        elif b == "C":
            entry.delete(0, 'end')
            result_label.config(text="")
        else:
            entry.insert('end', b)
    
    Button(root, text=button, width=5, height=2, font=('Arial', 14), command=on_click).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Label to display results
result_label = Label(root, text="", font=('Arial', 16))
result_label.grid(row=row_val, column=0, columnspan=4, pady=10)

# Run the Tkinter event loop
root.mainloop()
