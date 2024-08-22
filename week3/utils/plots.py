# utils/plots.py

import cv2
import numpy as np
import matplotlib.pyplot as plt

def initialize_subplot_grid(n_rows, n_cols, figsize=(15, 5)):
    """
    Initialize a grid of subplots for plotting.

    Parameters:
        n_rows (int): Number of rows in the subplot grid.
        n_cols (int): Number of columns in the subplot grid.
        figsize (tuple): Size of the figure.

    Returns:
        fig (Figure): The figure object.
        axes (array of Axes): Array of subplot axes.
    """
    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
    return fig, axes

def plot_monochrome_histogram(ax, img, title):
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    ax.set_title(title)
    ax.set_xlabel('Intensity')
    ax.set_ylabel('Frequency of occurrence')
    ax.plot(hist)


def plot_bgr_histogram(ax, img, title):
    """
    Plot histogram for an image on a given axis.

    Parameters:
        ax (Axes): The subplot axis to plot on.
        img (ndarray): The image to plot the histogram for.
        title (str): The title for the histogram plot.
    """
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hist_gray = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    hist_gray, bin_edges = np.histogram(gray_image.flatten(), bins = 256, range=(0, 256))
    channels = cv2.split(img)
    colors = ['b', 'g', 'r']

    ax.set_title(title)
    ax.set_xlabel('Pixel Value')
    ax.set_ylabel('Frequency')
    ax.plot(hist_gray, color='black', label='Gray')

    for clr, ch in zip(colors, channels):
        hist = cv2.calcHist([ch], [0], None, [256], [0, 256])
        ax.plot(hist, color=clr, label=clr.upper())
    ax.legend()

def plot_img(ax, img, title):
    """
    Plot an image on a given axis.

    Parameters:
        ax (Axes): The subplot axis to plot on.
        img (ndarray): The image to plot.
        title (str): The title for the image plot.
    """
    ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for display
    ax.set_title(title)
    ax.axis('off')