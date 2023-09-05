import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than 0.")
        return
    
    character_pool = ''
    if include_letters.get():
        character_pool += string.ascii_letters
    if include_digits.get():
        character_pool += string.digits
    if include_symbols.get():
        character_pool += string.punctuation
    
    if not character_pool:
        messagebox.showerror("Error", "Select at least one character type.")
        return
    
    password = ''.join(random.choice(character_pool) for _ in range(length))
    password_display.config(text=password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x300")
# Password length
length_label = ttk.Label(root, text="Password Length:")
length_label.pack()
length_entry = ttk.Entry(root)
length_entry.pack()

# Character type options
include_letters = tk.BooleanVar()
letters_checkbox = ttk.Checkbutton(root, text="Include Letters", variable=include_letters)
letters_checkbox.pack()
include_letters.set(True)  # Default to include letters

include_digits = tk.BooleanVar()
digits_checkbox = ttk.Checkbutton(root, text="Include Digits", variable=include_digits)
digits_checkbox.pack()
include_digits.set(True)  # Default to include digits

include_symbols = tk.BooleanVar()
symbols_checkbox = ttk.Checkbutton(root, text="Include Symbols", variable=include_symbols)
symbols_checkbox.pack()
include_symbols.set(True)  # Default to include symbols

# Generate button
generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Display generated password
password_display = ttk.Label(root, text="", font=("Helvetica", 12))
password_display.pack()

# Run the tkinter main loop
root.mainloop()
