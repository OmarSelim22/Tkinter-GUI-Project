import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import cv2
# Initialize global variables
original_image = None
displayed_image = None

root = tk.Tk()
root.title("Histogram & Enhancement")
root.geometry("1920x1080")
root.configure(bg = "#0a2a2f")


main_frame = tk.Frame(root, bg="#0a2a2f")
main_frame.pack(expand=True, fill="both", padx=20, pady=20)


buttons_frame = tk.Frame(main_frame, bg="#0a2a2f")
buttons_frame.pack(side="left", fill="y", padx=20)


tk.Label(buttons_frame, text="DIP Functions", fg="white", bg="#0a2a2f",
         font=("Arial", 18, "bold")).pack(pady=(0, 30))


def create_btn(text, command):
    return tk.Button(buttons_frame, text=text, width=25, height=2, command=command,
                     bg="#123c42", fg="white", font=("Arial", 10, "bold"), bd=0, relief="flat")

point_ops_frame = tk.Frame(main_frame, bg="#0a2a2f")
tk.Label(point_ops_frame, text="Point Operations", fg="white", bg="#0a2a2f",
         font=("Arial", 18, "bold")).pack(pady=(0, 30))

def create_btn1(parent, text, command):
    return tk.Button(parent, text=text, width=25, height=2, command=command,)

btn1 = create_btn1(point_ops_frame, "Button 1", lambda: print("Button 1 pressed"))
btn2 = create_btn1(point_ops_frame, "Button 2", lambda: print("Button 2 pressed"))

btn1.pack(pady=10)
btn2.pack(pady=10)
def switch_to_point_ops():
    buttons_frame.pack_forget()
    point_ops_frame.pack(side="left", fill="y", padx=20)
def switch_to_point_ops():
    buttons_frame.pack_forget()
    point_ops_frame.pack(side="left", fill="y", padx=20)


btn_show = create_btn("Show Original", lambda: show_image("original"))
btn_point_operations = create_btn("Point Operations", switch_to_point_ops)
btn_color_image_operations = create_btn("Colour Image Operations", lambda: process_image("equalize"))
btn_image_histogram = create_btn("Image Histogram", lambda: process_image("equalize"))
btn_neighborhood_processing = create_btn("Neighborhood Processing", lambda: process_image("equalize"))
btn_image_restoration = create_btn("Image Restoration", lambda: process_image("equalize"))
btn_image_segmentation = create_btn("Image Segmentation", lambda: process_image("equalize"))
btn_edge_detection = create_btn("Edge Detection", lambda: process_image("equalize"))
btn_mathematical_morphology = create_btn("Mathematical Morphology", lambda: process_image("equalize"))

btn_show.pack(pady=10)
btn_point_operations.pack(pady=10)
btn_color_image_operations.pack(pady=10)
btn_image_histogram.pack(pady=10)
btn_neighborhood_processing.pack(pady=10)
btn_image_restoration.pack(pady=10)
btn_image_segmentation.pack(pady=10)
btn_edge_detection.pack(pady=10)
btn_mathematical_morphology.pack(pady=10)

# Define the load_image function before using it
def load_image():
    global original_image, displayed_image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        original_image = Image.open(file_path)
        original_image = original_image.resize((1620 , 900))  # Resize to fit the display area
        displayed_image = None
        show_image("original")

btn_load = create_btn("Load Image", load_image)
btn_load.pack(pady=10)
# tk.Label(buttons_frame, text="Enhance", fg="gray", bg="#0a2a2f", font=("Arial", 12, "bold")).pack(pady=(30, 5))

# btn_light = create_btn("☀ Enhance Lighting", lambda: process_image("enhance"))
# btn_light.pack()


image_frame = tk.Frame(main_frame, bg="#0a2a2f", bd=2, relief="groove")
image_frame.pack(side="right", expand=True, fill="both", padx=20)

image_label = tk.Label(image_frame, bg="#0a2a2f")
image_label.pack(expand=True)

def load_image():
    global original_image, displayed_image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        original_image = Image.open(file_path)
        original_image = original_image.resize((400 , 400))  # Resize to fit the display area
        displayed_image = None
        show_image("original")

def show_image(mode):
    global displayed_image
    if mode == "original" and original_image:
        img = original_image.copy()
        img = img.resize((400, 400))
        displayed_image = ImageTk.PhotoImage(img)
        image_label.config(image=displayed_image)
        image_label.image = displayed_image  # Retain a reference to avoid garbage collection

def process_image(mode):
    print(f"Processing: {mode}")
    if mode == "stretch":
        # Implement histogram stretching logic here
        pass
    elif mode == "equalize":
        # Implement histogram equalization logic here
        pass
    elif mode == "enhance":
        # Implement lighting enhancement logic here
        pass

    if displayed_image:
        # Update the displayed image after processing
        img = original_image.copy()
        img = img.resize((400, 400))
        displayed_image = ImageTk.PhotoImage(img)
        image_label.config(image=displayed_image)
        image_label.image = displayed_image  # Retain a reference to avoid garbage collection



show_image("original")  # Show the original image when the app starts
# Set the initial image to None
root.mainloop()