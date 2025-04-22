import cv2
import numpy as np
from PIL import Image

def Adaptive_Thre(image):
    # Handle both path string and image input
    if isinstance(image, str):  # If path is provided
        img = cv2.imread(image, 0)
    else:  # Assume image is already loaded (PIL or numpy array)
        if isinstance(image, Image.Image):  # Convert PIL to numpy
            img = np.array(image)
            if len(img.shape) == 3:  # Convert to grayscale if RGB
                img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        else:  # Assume numpy array
            img = image.copy()
            if len(img.shape) == 3:  # Convert to grayscale if RGB
                img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    # Ensure minimum width of 256 pixels
    if img.shape[1] < 256:
        img = cv2.resize(img, (256, img.shape[0]))
    
    # Split into 4 equal vertical regions
    p1 = img[:, :64]
    p2 = img[:, 64:128]
    p3 = img[:, 128:192]
    p4 = img[:, 192:256]
    
    # Apply Otsu's threshold to each region
    _, im_th1 = cv2.threshold(p1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    _, im_th2 = cv2.threshold(p2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    _, im_th3 = cv2.threshold(p3, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    _, im_th4 = cv2.threshold(p4, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Combine the thresholded regions
    combined = np.concatenate((im_th1, im_th2, im_th3, im_th4), axis=1)
    return combined  # Return numpy array