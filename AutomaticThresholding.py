import cv2
import numpy as np
from PIL import Image

def Auto_Thre(image):
    # Handle different input types
    if isinstance(image, str):  # If path is provided
        img = cv2.imread(image, 0)
    elif isinstance(image, Image.Image):  # If PIL Image
        img = np.array(image)
        if len(img.shape) == 3:  # Convert to grayscale if RGB
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    else:  # Assume numpy array
        img = image.copy()
        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    # Automatic thresholding algorithm
    Theta = np.mean(img)
    done = False  
    while not done:
        p1_mask = img >= Theta
        p2_mask = ~p1_mask
        p1 = img[p1_mask]
        p2 = img[p2_mask]
        m1 = np.mean(p1) if len(p1) > 0 else Theta
        m2 = np.mean(p2) if len(p2) > 0 else Theta
        Th_next = 0.5 * (m1 + m2)
        done = abs(Theta - Th_next) < 0.5
        Theta = Th_next
    
    im_thr = np.where(img >= Theta, 255, 0).astype(np.uint8)
    return im_thr  # Return numpy array instead of PIL Image