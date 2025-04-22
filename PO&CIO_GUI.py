
# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog
# from PIL import Image, ImageTk, ImageOps
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# from tkinter import messagebox
# from tkinter import font as tkFont

# def create_tab1(tab):
#     def load_image():
#         file_path = filedialog.askopenfilename()
#         if file_path:
#             img = Image.open(file_path).convert("RGB")
#             img.thumbnail((400, 400))
#             image_label.img = ImageTk.PhotoImage(img)
#             image_label.config(image=image_label.img)
#             image_label.image_path = file_path

#     def save_image():
#         if hasattr(image_label, 'result_img'):
#             file_path = filedialog.asksaveasfilename(defaultextension=".png")
#             if file_path:
#                 image_label.result_img.save(file_path)

#     def apply_complement():
#         if hasattr(image_label, 'image_path'):
#             img = Image.open(image_label.image_path).convert("RGB")
#             comp = ImageOps.invert(img)
#             comp.thumbnail((400, 400))
#             result_img = ImageTk.PhotoImage(comp)
#             result_label.img = result_img
#             result_label.config(image=result_img)
#             image_label.result_img = comp
#             image_label.result_img.thumbnail((400, 400))
#             result_label.image_path = image_label.image_path        
#     def increase_brightness(img, value=30):
#         """Increase brightness of the image."""
#         img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
#         hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#         h, s, v = cv2.split(hsv)
#         v = np.clip(v + value, 0, 255)
#         hsv = cv2.merge((h, s, v))
#         img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
#         return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#     def decrease_brightness(img, value=30):
#         """Decrease brightness of the image."""
#         img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
#         hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#         h, s, v = cv2.split(hsv)
#         v = np.clip(v - value, 0, 255)
#         hsv = cv2.merge((h, s, v))
#         img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
#         return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#     def apply_brightness():
#         if hasattr(image_label, 'image_path'):
#             img = Image.open(image_label.image_path).convert("RGB")
#             bright_img = increase_brightness(img, value=30)
#             bright_img.thumbnail((400, 400))
#             result_img = ImageTk.PhotoImage(bright_img)
#             result_label.img = result_img
#             result_label.config(image=result_img)
#             image_label.result_img = bright_img
#             image_label.result_img.thumbnail((400, 400))
#             result_label.image_path = image_label.image_path
#     def apply_decrease_brightness():
#         if hasattr(image_label, 'image_path'):
#             img = Image.open(image_label.image_path).convert("RGB")
#             bright_img = decrease_brightness(img, value=30)
#             bright_img.thumbnail((400, 400))
#             result_img = ImageTk.PhotoImage(bright_img)
#             result_label.img = result_img
#             result_label.config(image=result_img)
#             image_label.result_img = bright_img
#             image_label.result_img.thumbnail((400, 400))
#             result_label.image_path = image_label.image_path
#     def apply_contrast():
#         if hasattr(image_label, 'image_path'):
#             img = Image.open(image_label.image_path).convert("RGB")
#             contrast_img = ImageOps.autocontrast(img)
#             contrast_img.thumbnail((400, 400))
#             result_img = ImageTk.PhotoImage(contrast_img)
#             result_label.img = result_img
#             result_label.config(image=result_img)
#             image_label.result_img = contrast_img
#             image_label.result_img.thumbnail((400, 400))
#             result_label.image_path = image_label.image_path
#     def show_original():
#         if hasattr(image_label, 'image_path'):
#             img = Image.open(image_label.image_path).convert("RGB")
#             img.thumbnail((400, 400))
#             original_img = ImageTk.PhotoImage(img)
#             image_label.img = original_img
#             image_label.config(image=original_img)
#             image_label.result_img = img
#             image_label.result_img.thumbnail((400, 400))
#             image_label.image_path = image_label.image_path
#     def show_result_plot():
#         if hasattr(image_label, 'result_img'):
#             import matplotlib.pyplot as plt
#             plt.figure(figsize=(6, 6))
#             plt.imshow(image_label.result_img)
#             plt.title("Result")
#             plt.axis('off')
#             plt.show()
#     def show_original_plot():
#         if hasattr(image_label, 'image_path'):
#             img = Image.open(image_label.image_path).convert("RGB")
#             plt.figure(figsize=(6, 6))
#             plt.imshow(img)
#             plt.title("Original")
#             plt.axis('off')
#             plt.show()
#     def show_complement_plot():
#         if hasattr(image_label, 'result_img'):
#             img = ImageOps.invert(image_label.result_img)
#             plt.figure(figsize=(6, 6))
#             plt.imshow(img)
#             plt.title("Complement")
#             plt.axis('off')
#             plt.show()
#     def show_brightness_plot():
#         if hasattr(image_label, 'result_img'):
#             img = increase_brightness(image_label.result_img, value=30)
#             plt.figure(figsize=(6, 6))
#             plt.imshow(img)
#             plt.title("Brightness")
#             plt.axis('off')
#             plt.show()
#     def show_decrease_brightness_plot():
#         if hasattr(image_label, 'result_img'):
#             img = decrease_brightness(image_label.result_img, value=30)
#             plt.figure(figsize=(6, 6))
#             plt.imshow(img)
#             plt.title("Decrease Brightness")
#             plt.axis('off')
#             plt.show()
#     def show_contrast_plot():
#         if hasattr(image_label, 'result_img'):
#             img = ImageOps.autocontrast(image_label.result_img)
#             plt.figure(figsize=(6, 6))
#             plt.imshow(img)
#             plt.title("Contrast")
#             plt.axis('off')
#             plt.show()
#     def show_histogram_plot():
#         if hasattr(image_label, 'result_img'):
#             img = np.array(image_label.result_img)
#             plt.figure(figsize=(6, 6))
#             plt.hist(img.ravel(), bins=256, color='gray', alpha=0.7)
#             plt.title("Histogram")
#             plt.xlabel("Pixel Value")
#             plt.ylabel("Frequency")
#             plt.xlim([0, 255])
#             plt.show()
#     def show_histogram():
#         if hasattr(image_label, 'result_img'):
#             img = np.array(image_label.result_img)
#             hist = cv2.calcHist([img], [0], None, [256], [0, 256])
#             plt.figure(figsize=(6, 6))
#             plt.plot(hist)
#             plt.title("Histogram")
#             plt.xlabel("Pixel Value")
#             plt.ylabel("Frequency")
#             plt.xlim([0, 255])
#             plt.show()
   

#     def apply_addition():
#         if hasattr(image_label, 'image_path'):
#             img = Image.open(image_label.image_path).convert("RGB")
#             img = np.array(img).astype(np.int32)  # prevent overflow
#             add_img = np.clip(img + 20, 0, 255).astype(np.uint8)
#             add_img = Image.fromarray(add_img)
#             add_img.thumbnail((400, 400))
#             result_img = ImageTk.PhotoImage(add_img)
#             result_label.img = result_img
#             result_label.config(image=result_img)
#             image_label.result_img = add_img
#             image_label.result_img.thumbnail((400, 400))
#             result_label.image_path = image_label.image_path
#     # Create buttons and labels
#     def apply_subtraction():
#         if hasattr(image_label, 'image_path'):
#             img = Image.open(image_label.image_path).convert("RGB")
#             img = np.array(img).astype(np.int32)
#             sub_img = np.clip(img - 20, 0, 255).astype(np.uint8)
#             sub_img = Image.fromarray(sub_img)
#             sub_img.thumbnail((400, 400))
#             result_img = ImageTk.PhotoImage(sub_img)
#             result_label.img = result_img
#             result_label.config(image=result_img)
#             image_label.result_img = sub_img
#             image_label.result_img.thumbnail((400, 400))
#             result_label.image_path = image_label.image_path
#     def apply_multiplication():
#         if hasattr(image_label, 'image_path'):
#             img = Image.open(image_label.image_path).convert("RGB")
#             img = np.array(img).astype(np.int32)
#             mul_img = np.clip(img * 2, 0, 255).astype(np.uint8)
#             mul_img = Image.fromarray(mul_img)
#             mul_img.thumbnail((400, 400))
#             result_img = ImageTk.PhotoImage(mul_img)
#             result_label.img = result_img
#             result_label.config(image=result_img)
#             image_label.result_img = mul_img
#             image_label.result_img.thumbnail((400, 400))
#             result_label.image_path = image_label.image_path
#     def apply_division():
#         if hasattr(image_label, 'image_path'):
#             img = Image.open(image_label.image_path).convert("RGB")
#             img = np.array(img).astype(np.int32)
#             div_img = np.clip(img // 2, 0, 255).astype(np.uint8)
#             div_img = Image.fromarray(div_img)
#             div_img.thumbnail((400, 400))
#             result_img = ImageTk.PhotoImage(div_img)
#             result_label.img = result_img
#             result_label.config(image=result_img)
#             image_label.result_img = div_img
#             image_label.result_img.thumbnail((400, 400))
#             result_label.image_path = image_label.image_path

#     image_label = tk.Label(tab)
#     image_label.pack(side="left", padx=10, pady=10)

#     result_label = tk.Label(tab)
#     result_label.pack(side="right", padx=10, pady=10)

#     btn_load = tk.Button(tab, text="Load Image", command=load_image)
#     btn_load.pack(pady=5)

#     btn_complement = tk.Button(tab, text="Complement", command=apply_complement)
#     btn_complement.pack(pady=5)
#     btn_brightness = tk.Button(tab, text="Increase Brightness", command=apply_brightness)
#     btn_brightness.pack(pady=5)
#     btn_decrease_brightness = tk.Button(tab, text="Decrease Brightness", command=apply_decrease_brightness)     
#     btn_decrease_brightness.pack(pady=5)
#     btn_contrast = tk.Button(tab, text="Contrast", command=apply_contrast)
#     btn_contrast.pack(pady=5)
#     btn_show_original = tk.Button(tab, text="Show Original", command=show_original)
#     btn_show_original.pack(pady=5)
#     btn_show_result = tk.Button(tab, text="Show Result", command=show_result_plot)
#     btn_show_result.pack(pady=5)
#     btn_show_original_plot = tk.Button(tab, text="Show Original Plot", command=show_original_plot)
#     btn_show_original_plot.pack(pady=5)
#     btn_show_complement_plot = tk.Button(tab, text="Show Complement Plot", command=show_complement_plot)
#     btn_show_complement_plot.pack(pady=5)
#     btn_show_brightness_plot = tk.Button(tab, text="Show Brightness Plot", command=show_brightness_plot)
#     btn_show_brightness_plot.pack(pady=5)
#     btn_show_decrease_brightness_plot = tk.Button(tab, text="Show Decrease Brightness Plot", command=show_decrease_brightness_plot) 
#     btn_addition = tk.Button(tab, text="Show Plot", command=apply_addition)
#     btn_addition.pack(pady=5)
   

#     btn_save = tk.Button(tab, text="Save Result", command=save_image)
#     btn_save.pack(pady=5)

#     # Set the background color of the tab
#     tab.configure(bg='#1e1e1e')
#     # Set the title of the tab
#     title = tk.Label(tab, text="Point Operations", font=("Helvetica", 18), fg="white", bg="#1e1e1e")
#     title.pack(pady=10)
#     # Set the button colors
#     btn_load.configure(bg="#4CAF50", fg="white")
#     btn_complement.configure(bg="#2196F3", fg="white")
#     btn_save.configure(bg="#FF9800", fg="white")
#     # Set the label colors
#     image_label.configure(bg="#1e1e1e")
#     result_label.configure(bg="#1e1e1e")
#     # Set the tab color
#     tab.configure(bg="#1e1e1e")
#     # Set the button colors         
#     btn_load.configure(bg="#4CAF50", fg="white")            
#     btn_complement.configure(bg="#2196F3", fg="white")
#     btn_save.configure(bg="#FF9800", fg="white")
   
# #example usage
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Image Processing Application")
#     root.geometry("800x600")

#     # Create a tabbed interface
#     tab_control = tk.ttk.Notebook(root)
#     tab1 = tk.Frame(tab_control, bg='#1e1e1e')
#     tab_control.add(tab1, text="Point Operations")
#     tab_control.pack(expand=1, fill="both")

#     create_tab1(tab1)

#     root.mainloop()
# import tkinter as tk
# from tkinter import filedialog, messagebox
# from PIL import Image, ImageTk, ImageOps
# import numpy as np
# import cv2

# # Global variables
# original_img = None
# displayed_image = None

# # Main GUI setup
# root = tk.Tk()
# root.title("Point & Color Image Operations")
# root.geometry("1920x1080")
# root.configure(bg="#0a2a2f")

# # Hover Functions
# def on_enter(button):
# 	button.widget["background"] = "lightblue"
# 	button.widget["fg"] = "black"

# def on_leave(button):
# 	button.widget["background"] = "#123c42"
# 	button.widget["fg"] = "white"

# # Main frame setup
# main_frame = tk.Frame(root, bg="#0a2a2f")
# main_frame.pack(expand=True, fill="both", padx=20, pady=20)

# # Left panel with buttons
# buttons_frame = tk.Frame(main_frame, bg="#0a2a2f")
# buttons_frame.pack(side="left", fill="y", padx=20)

# canvas = tk.Canvas(buttons_frame, bg="#0a2a2f", highlightthickness=0)
# scrollbar = tk.Scrollbar(buttons_frame, orient="vertical", command=canvas.yview)
# scrollable_frame = tk.Frame(canvas, bg="#0a2a2f")

# canvas.configure(yscrollcommand=scrollbar.set)
# canvas.pack(side="left", fill="y", expand=True)
# scrollbar.pack(side="right", fill="y")

# canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# def configure_scrollregion(event):
# 	canvas.configure(scrollregion=canvas.bbox("all"))

# scrollable_frame.bind("<Configure>", configure_scrollregion)

# def on_mousewheel(event):
# 	canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

# canvas.bind_all("<MouseWheel>", on_mousewheel)

# # Image display frame
# image_frame = tk.Frame(main_frame, bg="#0a2a2f", bd=2, relief="groove")
# image_frame.pack(side="right", expand=True, fill="both", padx=20)

# image_label = tk.Label(image_frame, bg="#0a2a2f")
# image_label.pack(expand=True)

# # UI components
# def create_section(title):
# 	tk.Label(scrollable_frame, text=title, fg="white", bg="#0a2a2f", font=("Arial", 18, "bold")).pack(pady=(10, 5))
# 	tk.Frame(scrollable_frame, height=1, bg="#2d6b74").pack(fill="x", pady=(0, 10))

# def create_btn(text, command):
# 	btn = tk.Button(scrollable_frame, text=text, width=25, height=2, command=command, bg="#123c42", fg="white", font=("Arial", 10, "bold"), bd=0, relief="flat")
# 	btn.bind("<Enter>", on_enter)
# 	btn.bind("<Leave>", on_leave)
# 	return btn

# #Functions

# def load_image():
# 	global original_img, displayed_image
# 	path = filedialog.askopenfilename()
# 	if path:
# def show_original():
# 	if original_img:
# def apply_complement():
# 	if original_img:
# 		inverted = ImageOps.invert(original_img)
# 		show_image(inverted)
# def add_const():
# 	if original_img:
# def sub_const():
# 	if original_img:
# def mul_const():
# 	if original_img:
# def div_const():
# 	if original_img:
# 		img = np.array(original_img).astype(np.int32)
# 		img = np.clip(img // 2, 0, 255).astype(np.uint8)
# def clear_image():
# 	global original_img, displayed_image
# 	original_img = None
# 	displayed_image = None
# 	image_label.config(image=None)
# 	image_label.image = None
# create_section("Load & Show Image")
# create_btn("Load Image", load_image).pack(pady=5)
# create_btn("Show Original", show_original).pack(pady=5)
# 		img = np.clip(img * 2, 0, 255).astype(np.uint8)
# 		show_image(Image.fromarray(img))
# 		img = np.clip(img - 20, 0, 255).astype(np.uint8)
# create_section("More Options")
# create_btn("Save Image", save_image).pack(pady=5)
# create_btn("Clear Image", clear_image).pack(pady=5)
# create_btn("Back", go_back).pack(pady=5)
# 		img = np.clip(img + 20, 0, 255).astype(np.uint8)
# 		show_image(Image.fromarray(img))
# 		show_image(original_img)

# def show_image(img): global displayed_image frame_width = image_label.winfo_width() or 1100 frame_height = image_label.winfo_height() or 800 resized = img.copy().resize((frame_width, frame_height)) displayed_image = ImageTk.PhotoImage(resized) image_label.config(image=displayed_image) image_label.image = displayed_image image_label.image_pil = img

# def show_original(): if original_img: show_image(original_img)

# def apply_complement(): if original_img: inverted = ImageOps.invert(original_img) show_image(inverted)

# def change_brightness(val): if original_img: hsv = cv2.cvtColor(np.array(original_img), cv2.COLOR_RGB2HSV) h, s, v = cv2.split(hsv) v = np.clip(v + val, 0, 255).astype(np.uint8) final = cv2.merge((h, s, v)) result = cv2.cvtColor(final, cv2.COLOR_HSV2RGB) show_image(Image.fromarray(result))

# def add_const(): if original_img: img = np.array(original_img).astype(np.int32) img = np.clip(img + 20, 0, 255).astype(np.uint8) show_image(Image.fromarray(img))

# def sub_const(): if original_img: img = np.array(original_img).astype(np.int32) img = np.clip(img - 20, 0, 255).astype(np.uint8) show_image(Image.fromarray(img))

# def mul_const(): if original_img: img = np.array(original_img).astype(np.int32) img = np.clip(img * 2, 0, 255).astype(np.uint8) show_image(Image.fromarray(img))

# def div_const(): if original_img: img = np.array(original_img).astype(np.int32) img = np.clip(img // 2, 0, 255).astype(np.uint8) show_image(Image.fromarray(img))

# def save_image(): if hasattr(image_label, 'image_pil') and image_label.image_pil: save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", ".png"), ("JPEG files", ".jpg"), ("All files", ".")]) if save_path: image_label.image_pil.save(save_path)

# def clear_image(): global original_img, displayed_image original_img = None displayed_image = None image_label.config(image=None) image_label.image = None image_label.image_pil = None

# def go_back(): root.destroy()

# #Layout the interface

# create_section("Load & Show Image") create_btn("Load Image", load_image).pack(pady=5) create_btn("Show Original", show_original).pack(pady=5)

# create_section("Point Operations") create_btn("Complement", apply_complement).pack(pady=5) create_btn("Increase Brightness", lambda: change_brightness(30)).pack(pady=5) create_btn("Decrease Brightness", lambda: change_brightness(-30)).pack(pady=5)

# create_section("Color Image Operations") create_btn("Addition (+20)", add_const).pack(pady=5) create_btn("Subtraction (-20)", sub_const).pack(pady=5) create_btn("Multiplication (*2)", mul_const).pack(pady=5) create_btn("Division (//2)", div_const).pack(pady=5)

# create_section("More Options") create_btn("Save Image", save_image).pack(pady=5) create_btn("Clear Image", clear_image).pack(pady=5) create_btn("Back", go_back).pack(pady=5)

# root.mainloop()



import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageOps
import numpy as np
import cv2

# Global variables
original_img = None
displayed_image = None

# Main GUI setup
root = tk.Tk()
root.title("Point & Color Image Operations")
root.geometry("1920x1080")
root.configure(bg="#0a2a2f")

# Hover Functions
def on_enter(event):
	event.widget["background"] = "lightblue"
	event.widget["fg"] = "black"

def on_leave(event):
	event.widget["background"] = "#123c42"
	event.widget["fg"] = "white"

# Main frame setup
main_frame = tk.Frame(root, bg="#0a2a2f")
main_frame.pack(expand=True, fill="both", padx=20, pady=20)

# Left panel with buttons
buttons_frame = tk.Frame(main_frame, bg="#0a2a2f")
buttons_frame.pack(side="left", fill="y", padx=20)

canvas = tk.Canvas(buttons_frame, bg="#0a2a2f", highlightthickness=0)
scrollbar = tk.Scrollbar(buttons_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#0a2a2f")

canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="y", expand=True)
scrollbar.pack(side="right", fill="y")

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

def configure_scrollregion(event):
	canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", configure_scrollregion)

def on_mousewheel(event):
	canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", on_mousewheel)

# Image display frame
image_frame = tk.Frame(main_frame, bg="#0a2a2f", bd=2, relief="groove")
image_frame.pack(side="right", expand=True, fill="both", padx=20)

image_label = tk.Label(image_frame, bg="#0a2a2f")
image_label.pack(expand=True)

# UI components
def create_section(title):
	tk.Label(scrollable_frame, text=title, fg="white", bg="#0a2a2f", font=("Arial", 18, "bold")).pack(pady=(10, 5))
	tk.Frame(scrollable_frame, height=1, bg="#2d6b74").pack(fill="x", pady=(0, 10))

def create_btn(text, command):
	btn = tk.Button(scrollable_frame, text=text, width=25, height=2, command=command, bg="#123c42", fg="white", font=("Arial", 10, "bold"), bd=0, relief="flat")
	btn.bind("<Enter>", on_enter)
	btn.bind("<Leave>", on_leave)
	return btn

# Functions
def load_image():
	global original_img, displayed_image
	path = filedialog.askopenfilename()
	if path:
		original_img = Image.open(path).convert("RGB")
		displayed_image = None
		show_image(original_img)

def show_image(img):
	global displayed_image
	frame_width = image_frame.winfo_width() or 1100
	frame_height = image_frame.winfo_height() or 800
	resized = img.copy().resize((frame_width, frame_height))
	displayed_image = ImageTk.PhotoImage(resized)
	image_label.config(image=displayed_image)
	image_label.image = displayed_image
	image_label.image_pil = img


def show_original():
	if original_img:
		show_image(original_img)

def img_complement(image):
    height, width = image.shape
    complemented_img = np.zeros((height,width), dtype=np.uint8)
    
    for i in range(height):
        for j in range(width):
            val = 255 - image[i,j]
            if val > 255:
                complemented_img[i,j] = 255
            elif val < 0:
                complemented_img[i,j] = 0
            else:
                complemented_img[i,j] = val

    
    return complemented_img

def change_brightness(val):
	if original_img:
		hsv = cv2.cvtColor(np.array(original_img), cv2.COLOR_RGB2HSV)
		h, s, v = cv2.split(hsv)
		v = np.clip(v + val, 0, 255).astype(np.uint8)
		final = cv2.merge((h, s, v))
		result = cv2.cvtColor(final, cv2.COLOR_HSV2RGB)
		show_image(Image.fromarray(result))

def add_const():
	if original_img:
		img = np.array(original_img).astype(np.int32)
		img = np.clip(img + 20, 0, 255).astype(np.uint8)
		img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		show_image(Image.fromarray(img_RGB))

def sub_const():
	if original_img:
		img = np.array(original_img).astype(np.int32)
		img = np.clip(img - 20, 0, 255).astype(np.uint8)
		img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		show_image(Image.fromarray(img_RGB))

def mul_const():
	if original_img:
		img = np.array(original_img).astype(np.int32)
		img = np.clip(img * 2, 0, 255).astype(np.uint8)
		img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		show_image(Image.fromarray(img_RGB))

def div_const():
	if original_img:
		img = np.array(original_img).astype(np.int32)
		img = np.clip(img // 2, 0, 255).astype(np.uint8)
		img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		show_image(Image.fromarray(img_RGB))

def save_image():
	if hasattr(image_label, 'image_pil') and image_label.image_pil:
		save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", ".png"), ("JPEG files", ".jpg"), ("All files", ".")])
		if save_path:
			image_label.image_pil.save(save_path)
def apply_complement():
	if original_img:
		inverted = ImageOps.invert(original_img)
		show_image(inverted)


def clear_image():
	global original_img, displayed_image
	original_img = None
	displayed_image = None
	image_label.config(image=None)
	image_label.image = None
	image_label.image_pil = None

def go_back():
	root.destroy()

# Layout the interface
create_section("Load & Show Image")
create_btn("Load Image", load_image).pack(pady=5)
create_btn("Show Original", show_original).pack(pady=5)

create_section("Point Operations")
create_btn("Complement", apply_complement).pack(pady=5)
create_btn("Increase Brightness", lambda: change_brightness(30)).pack(pady=5)
create_btn("Decrease Brightness", lambda: change_brightness(-30)).pack(pady=5)

create_section("Color Image Operations")
create_btn("Addition (+20)", add_const).pack(pady=5)
create_btn("Subtraction (-20)", sub_const).pack(pady=5)
create_btn("Multiplication (*2)", mul_const).pack(pady=5)
create_btn("Division (//2)", div_const).pack(pady=5)

create_section("More Options")
create_btn("Save Image", save_image).pack(pady=5)
create_btn("Clear Image", clear_image).pack(pady=5)
create_btn("Back", go_back).pack(pady=5)

root.mainloop()