import cv2
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk

def cv2_to_tkimg(cv_image):
    # Convert BGR to RGB
    rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    # Convert to PIL Image
    pil_image = Image.fromarray(rgb_image)
    # Convert to ImageTk format
    tk_image = ImageTk.PhotoImage(image=pil_image)
    return tk_image

def display_image(image_path):
    # Load image with OpenCV
    cv_image = cv2.imread(image_path)
    # Convert OpenCV image to Tkinter-compatible image
    tk_image = cv2_to_tkimg(cv_image)
    # Create a Label widget to hold the image
    label = tk.Label(root, image=tk_image)
    label.image = tk_image  # Keep a reference to avoid garbage collection
    label.pack()

# Create the main window
root = tk.Tk()
root.title("OpenCV and Tkinter")

# Display an image
display_image('./images/skull.png')

# Start the Tkinter event loop
root.mainloop()
