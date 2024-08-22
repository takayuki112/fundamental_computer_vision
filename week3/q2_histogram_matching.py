import cv2
import numpy as np
import matplotlib.pyplot as plt

from utils.plots import(
                initialize_subplot_grid,
                plot_img,
                plot_bgr_histogram,
                plot_monochrome_histogram
                )

from utils.image import(
                resize,
                histogram_matching_grey
                )

img = cv2.imread('./images/tree.png', 0)
ref = cv2.imread('./images/reference_tree.png')

new = histogram_matching_grey(img, ref)

# Initialize subplot grid
fig, axes = initialize_subplot_grid(n_rows=2, n_cols=3, figsize=(15, 7))

plot_img(axes[0, 0], img, 'Original Image')
plot_img(axes[0, 1], ref, 'Reference Image')
plot_img(axes[0, 2], new, 'Histogram Matched Image')

plot_monochrome_histogram(axes[1, 0], img, 'Original Image Histogram')
plot_monochrome_histogram(axes[1, 1], ref, 'Reference Image Histogram')
plot_monochrome_histogram(axes[1, 2], new, 'Histogram Matched Image Histogram')

plt.tight_layout()
plt.show()

