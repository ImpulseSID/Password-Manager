import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive integer for length")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Enter password length:").grid(row=0, column=0)
length_entry = tk.Entry(frame)
length_entry.grid(row=0, column=1)

generate_btn = tk.Button(frame, text="Generate", command=generate_password)
generate_btn.grid(row=1, column=0, columnspan=2, pady=5)

password_entry = tk.Entry(frame, width=30)
password_entry.grid(row=2, column=0, columnspan=2)

copy_btn = tk.Button(frame, text="Copy", command=copy_to_clipboard)
copy_btn.grid(row=3, column=0, columnspan=2, pady=5)

root.mainloop()
