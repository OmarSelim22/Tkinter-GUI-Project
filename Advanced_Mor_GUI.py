# Ensure ttkbootstrap is installed by running the following command in your terminal:
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter
import numpy as np
import cv2
import ttkbootstrap as tb

# ==== Morphological Operations ====
def get_mask():
    return np.ones((3, 3), dtype=np.uint8)

def dilate(image: np.ndarray) -> np.ndarray:
    padded = np.pad(image, 1, mode='constant', constant_values=0)
    output = np.zeros_like(image)
    mask = get_mask()
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            neighborhood = padded[i:i + 3, j:j + 3]
            if np.any(neighborhood * mask):
                output[i, j] = 255
    return output

def erode(image: np.ndarray) -> np.ndarray:
    padded = np.pad(image, 1, mode='constant', constant_values=0)
    output = np.zeros_like(image)
    mask = get_mask()
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            neighborhood = padded[i:i + 3, j:j + 3]
            if np.all(neighborhood * mask == 255):
                output[i, j] = 255
    return output

def opening(image: np.ndarray) -> np.ndarray:
    return dilate(erode(image))

def internal_boundary(image: np.ndarray) -> np.ndarray:
    return image - erode(image)

def external_boundary(image: np.ndarray) -> np.ndarray:
    return dilate(image) - image

def morphological_gradient(image: np.ndarray) -> np.ndarray:
    return dilate(image) - erode(image)

# ==== GUI ====
class MorphologyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Morphology Operations")
        self.root.geometry("1024x1020")
        self.root.configure(bg='#101820')

        self.image = None
        self.result = None
        self.original_pil = None  # Save original PIL image for filters

        title = tk.Label(root, text="Morphology Operations", font=("Arial",18, "bold"), fg="white", bg="blue")
        title.pack(pady=10)

        frame = tk.Frame(root, bg="#101820")
        frame.pack(pady=5)

        # Buttons on the left
        button_frame = tk.Frame(frame, bg="#101820")
        button_frame.grid(row=0, column=0, padx=20)

        buttons = [
            ("Load Image", self.load_image),
            ("Dilation", self.apply_dilate),
            ("Erosion", self.apply_erode),
            ("Opening", self.apply_opening),
            ("Internal Boundary", self.apply_internal_boundary),
            ("External Boundary", self.apply_external_boundary),
            ("Morphological Gradient", self.apply_gradient)
        ]

        for text, command in buttons:
            btn = tb.Button(button_frame, text=text, command=command, bootstyle="fg", width=20)
            btn.pack(pady=5)

        # Output & Original image
        image_frame = tk.Frame(frame, bg="#101820", bd=2)
        image_frame.grid(row=0, column=1, padx=20)

        self.original_label = tk.Label(image_frame, text="Original", fg="white", bg="#101820", font=("Arial", 10))
        self.original_label.pack()
        self.img_label = tk.Label(image_frame, bg="#101820")
        self.img_label.pack(padx=10, pady=5)

        self.result_label = tk.Label(image_frame, text="Result", fg="white", bg="#101820", font=("Arial", 10))
        self.result_label.pack()
        self.res_label = tk.Label(image_frame, bg="#101820")
        self.res_label.pack(padx=10, pady=5)

        # Bottom Filters
        bottom_frame = tk.Frame(root, bg="#101820")
        bottom_frame.pack(pady=10)

        tb.Button(bottom_frame, text="Filters", bootstyle="dark-outline", width=12, command=self.apply_filter).pack(side="left", padx=8)
        tb.Button(bottom_frame, text="Blur", bootstyle="dark-outline", width=12, command=self.apply_blur).pack(side="left", padx=8)
        tb.Button(bottom_frame, text="Contour", bootstyle="dark-outline", width=12, command=self.apply_contour).pack(side="left", padx=8)
        tb.Button(bottom_frame, text="Detail", bootstyle="dark-outline", width=12, command=self.apply_detail).pack(side="left", padx=8)
        tb.Button(bottom_frame, text="Save", bootstyle="dark-outline", width=12, command=self.save_result).pack(side="left", padx=8)

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (250, 250))
            self.image = img
            self.original_pil = Image.open(file_path).resize((250, 250))
            self.display_image(self.img_label, img)

    def display_image(self, label, img_array):
        img = Image.fromarray(img_array)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.config(image=imgtk)

    def display_pil_image(self, label, pil_img):
        img = pil_img.convert("RGB")
        self.result = np.array(img.convert("L"))  # Convert to grayscale for consistency
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.config(image=imgtk)

    def save_result(self):
        if self.result is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".png")
            if file_path:
                cv2.imwrite(file_path, self.result)

    def apply_dilate(self):
        if self.image is not None:
            self.result = dilate(self.image)
            self.display_image(self.res_label, self.result)

    def apply_erode(self):
        if self.image is not None:
            self.result = erode(self.image)
            self.display_image(self.res_label, self.result)

    def apply_opening(self):
        if self.image is not None:
            self.result = opening(self.image)
            self.display_image(self.res_label, self.result)

    def apply_internal_boundary(self):
        if self.image is not None:
            self.result = internal_boundary(self.image)
            self.display_image(self.res_label, self.result)

    def apply_external_boundary(self):
        if self.image is not None:
            self.result = external_boundary(self.image)
            self.display_image(self.res_label, self.result)

    def apply_gradient(self):
        if self.image is not None:
            self.result = morphological_gradient(self.image)
            self.display_image(self.res_label, self.result)

    # ===== Filters =====
    def apply_filter(self):
        if self.original_pil:
            filtered = self.original_pil.filter(ImageFilter.EDGE_ENHANCE_MORE)
            self.display_pil_image(self.res_label, filtered)

    def apply_blur(self):
        if self.original_pil:
            blurred = self.original_pil.filter(ImageFilter.GaussianBlur(radius=2))
            self.display_pil_image(self.res_label, blurred)

    def apply_contour(self):
        if self.original_pil:
            contoured = self.original_pil.filter(ImageFilter.CONTOUR)
            self.display_pil_image(self.res_label, contoured)

    def apply_detail(self):
        if self.original_pil:
            detailed = self.original_pil.filter(ImageFilter.DETAIL)
            self.display_pil_image(self.res_label, detailed)

# ==== Run App ====
if __name__ == "__main__":
    root = tb.Window(themename="darkly")
    app = MorphologyGUI(root)
    root.mainloop()
# This code is a simple GUI application for performing morphological operations on images using Tkinter and OpenCV.
# It includes functions for loading images, applying various morphological operations (dilation, erosion, opening, etc.),