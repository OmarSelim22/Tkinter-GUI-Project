import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import subprocess

root = tk.Tk()
root.title("Main Image Processing GUI")
root.geometry("1280x800")
root.configure(bg="#0a2a2f")

loaded_image = None
image_label = None
original_image = None  # to keep a copy for undo
zoom_level = 1.0

# --- Status Bar ---
status_var = tk.StringVar()
status_bar = tk.Label(root, textvariable=status_var, bg="#123c42", fg="white", anchor="w", height=2, font=("Arial", 9))
status_bar.pack(side="bottom", fill="x")
status_var.set("Ready")

# --- Header Bar ---
header = tk.Frame(root, bg="#123c42", height=50)
header.pack(side="top", fill="x")
tk.Label(header, text="📷  Main Image Processing GUI", bg="#123c42", fg="white", font=("Arial", 20, "bold")).pack(padx=10, pady=5, anchor="w")
# ---About us ---
def show_about():
    about_win = tk.Toplevel(root)
    about_win.title("About")
    tk.Label(about_win, text="Image Processing Project\nDeveloped by: Omer, Zaid, MenaAllah, Malak, Aliaa", font=("Arial", 12)).pack(padx=20, pady=20)
    tk.Button(about_win, text="Close", command=about_win.destroy).pack(pady=10)
    about_win.configure(bg="#0a2a2f")
    about_win.geometry("300x200")
    about_win.resizable(False, False)
header.bind("<Button-1>", lambda e: show_about())  # Click on header to show about
header.bind("<Enter>", lambda e: header.config(bg="#0a2a2f"))  # Change color on hover
header.bind("<Leave>", lambda e: header.config(bg="#123c42"))  # Revert color on leave


# --- Load Image ---
def load_image():
    global loaded_image, image_label, original_image, zoom_level
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")])
    if file_path:
        img = Image.open(file_path)
        img = img.resize((500, 400))
        original_image = img.copy()
        zoom_level = 1.0
        loaded_image = ImageTk.PhotoImage(img)
        image_label.config(image=loaded_image)
        image_label.image = loaded_image
        status_var.set("Image loaded successfully.")

# --- Save Image ---
def save_image():
    if loaded_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"),
                                                            ("JPEG files", "*.jpg"),
                                                            ("All files", ".")])
        if file_path:
            image_label.image._PhotoImage__photo.write(file_path, format="png")
            status_var.set("Image saved.")

# --- Undo ---
def undo_last_change():
    global loaded_image, original_image
    if original_image:
        img = original_image.copy()
        loaded_image = ImageTk.PhotoImage(img)
        image_label.config(image=loaded_image)
        image_label.image = loaded_image
        status_var.set("Undo applied.")

# --- Zoom Functions ---
def zoom_in():
    zoom(1.2)

def zoom_out():
    zoom(0.8)

def zoom(factor):
    global zoom_level, loaded_image, original_image
    if original_image:
        zoom_level *= factor
        new_size = (int(original_image.width * zoom_level), int(original_image.height * zoom_level))
        img = original_image.resize(new_size)
        loaded_image = ImageTk.PhotoImage(img)
        image_label.config(image=loaded_image)
        image_label.image = loaded_image
        status_var.set(f"Zoom: {int(zoom_level * 100)}%")

# --- External Modules ---
def open_page(module_name):
    subprocess.Popen(["python", module_name + ".py"])

# --- Exit Confirmation ---
def confirm_exit():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        root.destroy()

# --- Button Panel ---
buttons_frame = tk.Frame(root, bg="#0a2a2f")
buttons_frame.pack(side="left", fill="y", padx=20, pady=10)

def create_button(text, command, tooltip=""):
    btn = tk.Button(buttons_frame, text=text, width=25, height=2, command=command,
                    bg="#123c42", fg="white", font=("Arial", 10, "bold"), bd=0)
    btn.pack(pady=8)
    btn.bind("<Enter>", lambda e: [btn.config(bg="lightblue", fg="black"), status_var.set(tooltip)])
    btn.bind("<Leave>", lambda e: [btn.config(bg="#123c42", fg="white"), status_var.set("Ready")])
    return btn

tk.Label(buttons_frame, text="Main Menu", fg="white", bg="#0a2a2f", font=("Arial", 18, "bold")).pack(pady=(10, 20))

create_button("Load Image", load_image, "Load an image to process")
create_button("About Us", show_about, "Learn about the developers")
create_button("Save Image", save_image, "Save the current image")
create_button("Undo", undo_last_change, "Revert to original image")
create_button("Zoom In", zoom_in, "Zoom into the image")
create_button("Zoom Out", zoom_out, "Zoom out of the image")

tk.Label(buttons_frame, text="Filters & Operations", fg="white", bg="#0a2a2f", font=("Arial", 14, "bold")).pack(pady=(20, 10))
tk.Frame(buttons_frame, height=1, bg="#2d6b74").pack(fill="x", pady=(0, 10))

create_button("Histogram & Neighborhood", lambda: open_page("Histo_Neib_GUI"))
create_button("Restoration", lambda: open_page("Restoration_GUI"))
create_button("Morphology", lambda: open_page("Last_Morphology_GUI"))
create_button("Point & Color Ops", lambda: open_page("PO_CIO_GUI"))

create_button("Exit", confirm_exit, "Close the application")

# --- Image Display ---
right_frame = tk.Frame(root, bg="#0a2a2f")
right_frame.pack(side="right", expand=True, fill="both", padx=20, pady=20)

image_label = tk.Label(right_frame, bg="#0a2a2f")
image_label.pack(expand=True)

footer_label = tk.Label(
    root,
    text="Developed by Omer , Zaid , MenaAllah , Malak , Aliaa",  
    bg="#0a2a2f",
    fg="#b5d6d6",
    font=("Segoe UI", 10, "italic")
)
footer_label.place(relx=0.5, rely=0.98, anchor='center')
    
# --- Placeholder image ---
try:
    icon_image = Image.open("cameraman.png").resize((300, 300))
    icon_photo = ImageTk.PhotoImage(icon_image)
    icon_label = tk.Label(right_frame, image=icon_photo, bg="#0a2a2f")
    icon_label.pack(pady=20)
except Exception as e:
    print("Image not found:", e)

root.mainloop()

