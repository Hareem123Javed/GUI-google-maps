
import tkinter as tk
from tkinter import messagebox

# Hardcoded user credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "admin"

# Function to check login credentials
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        messagebox.showinfo("Login Successful", "Welcome!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Create the GUI window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x180")

# Username label and text entry box
tk.Label(root, text="Username").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack()

# Password label and password entry box
tk.Label(root, text="Password").pack(pady=5)
password_entry = tk.Entry(root, show='*')
password_entry.pack()

# Login button
tk.Button(root, text="Login", command=login).pack(pady=15)

root.mainloop()
