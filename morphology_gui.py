
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import cv2
from morphology import dilate, erode , opening, internal_boundary, external_boundary, morphological_gradient

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

class MorphologyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Morphological Operations")
        self.image = None
        self.result = None

        tk.Button(root, text="Load Image", command=self.load_image).pack()
        tk.Button(root, text="Dilation", command=self.apply_dilate).pack()
        tk.Button(root, text="Erosion", command=self.apply_erode).pack()
        tk.Button(root, text="Opening", command=self.apply_opening).pack()
        tk.Button(root, text="Internal Boundary", command=self.apply_internal_boundary).pack()
        tk.Button(root, text="External Boundary", command=self.apply_external_boundary).pack()
        tk.Button(root, text="Morphological Gradient", command=self.apply_gradient).pack()
        tk.Button(root, text="Save Result", command=self.save_result).pack()

        self.img_label = tk.Label(root)
        self.img_label.pack(side="left", padx=10, pady=10)

        self.res_label = tk.Label(root)
        self.res_label.pack(side="right", padx=10, pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (300, 300))
            self.image = img
            self.display_image(self.img_label, img)

    def save_result(self):
        if self.result is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".png")
            if file_path:
                cv2.imwrite(file_path, self.result)

    def display_image(self, label, img_array):
        img = Image.fromarray(img_array)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.config(image=imgtk)

    def apply_dilate(self):
        if self.image is not None:
            self.result = dilate(self.image)
            self.display_image(self.res_label, self.result)

    def apply_erode(self):
        if self.image is not None:
            self.result = erode(self.image)
            self.display_image(self.res_label, self.result)
            def show_result_plot(self): 
                if self.result is not None:
                    import matplotlib.pyplot as plt
                    plt.figure(figsize=(6, 6))
                    plt.imshow(self.result, cmap='gray')
                    plt.title("Result")
                    plt.axis('off')
                    plt.show()
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

if __name__ == "__main__":
    root = tk.Tk()
    app = MorphologyGUI(root)
    root.mainloop()
