import tkinter as tk
from tkinter import ttk
import Test111 as t1

def show_histogram():
    # Clear the window and show histogram page
    for widget in root.winfo_children():
        widget.destroy()
    
    label = ttk.Label(root, text="Histogram Page", font=('Arial', 14))
    label.pack(pady=50)
    
    back_button = ttk.Button(root, text="Back to Main", command=create_main_page)
    back_button.pack()

def show_restoration():
    # Clear the window and show restoration page
    for widget in root.winfo_children():
        widget.destroy()
    
    t1.test111(root)

def create_main_page():
    # Clear the window and create main page
    for widget in root.winfo_children():
        widget.destroy()
    
    # Main title
    title = ttk.Label(root, text="Image Processing Tool", font=('Arial', 16))
    title.pack(pady=20)
    
    # Histogram button
    hist_button = ttk.Button(
        root, 
        text="Histogram", 
        command=show_histogram,
        width=20
    )
    hist_button.pack(pady=10)
    
    # Restoration button
    restore_button = ttk.Button(
        root, 
        text="Restoration", 
        command=show_restoration,
        width=20
    )
    restore_button.pack(pady=10)

# Create main window
root = tk.Tk()
root.title("Image Processing Tool")
root.geometry("1920x1080")

# Start with main page
create_main_page()

# Run the application
root.mainloop()