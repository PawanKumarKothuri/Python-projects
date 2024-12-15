import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_var.get())
        if length < 1:
            raise ValueError("Length must be at least 1.")
        
        characters = string.ascii_lowercase
        if uppercase_var.get():
            characters += string.ascii_uppercase
        if numbers_var.get():
            characters += string.digits
        if special_var.get():
            characters += string.punctuation
        
        if not characters:
            messagebox.showerror("Error", "No character types selected!")
            return
        
        password = ''.join(random.choice(characters) for _ in range(length))
        password_var.set(password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def save_password():
    password = password_var.get()
    if password:
        with open("passwords.txt", "a") as file:
            file.write(password + "\n")
        messagebox.showinfo("Success", "Password saved successfully!")
    else:
        messagebox.showerror("Error", "No password to save!")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Variables
length_var = tk.StringVar()
uppercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
special_var = tk.BooleanVar()
password_var = tk.StringVar()

# Layout
tk.Label(root, text="Password Length:").pack(pady=5)
tk.Entry(root, textvariable=length_var).pack(pady=5)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).pack(pady=5)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack(pady=5)
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

tk.Label(root, text="Generated Password:").pack(pady=5)
tk.Entry(root, textvariable=password_var, state="readonly").pack(pady=5)

tk.Button(root, text="Save Password", command=save_password).pack(pady=5)

# Start the main loop
root.mainloop()
