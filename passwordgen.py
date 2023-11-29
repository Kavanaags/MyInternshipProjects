import tkinter as tk
from tkinter import ttk
import secrets
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def generate_passwords():
    length = int(length_entry.get())
    num_passwords = int(num_passwords_entry.get())

    passwords = [generate_password(length) for _ in range(num_passwords)]

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, '\n'.join(passwords))

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
length_label = ttk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = ttk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

num_passwords_label = ttk.Label(root, text="Number of Passwords:")
num_passwords_label.grid(row=1, column=0, padx=10, pady=10)

num_passwords_entry = ttk.Entry(root)
num_passwords_entry.grid(row=1, column=1, padx=10, pady=10)

generate_button = ttk.Button(root, text="Generate Passwords", command=generate_passwords)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_text = tk.Text(root, height=10, width=40)
result_text.grid(row=3, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()