import numpy as np
from PIL import Image

def Basic_Thre(image):
    # Convert input to numpy array if it isn't already
    if isinstance(image, Image.Image):  # If PIL Image
        img_array = np.array(image)
    elif isinstance(image, str):  # If path (shouldn't happen in your case)
        img_array = np.array(Image.open(image).convert('L'))
    else:  # Assume numpy array
        img_array = image
    
    # Ensure 2D grayscale (single channel)
    if len(img_array.shape) == 3:
        img_array = img_array[:,:,0]  # Take first channel if RGB
    
    # Apply threshold and ensure proper dtype
    binary_image = (img_array > 130).astype(np.uint8) * 255
    return binary_image  # Return numpy array directly