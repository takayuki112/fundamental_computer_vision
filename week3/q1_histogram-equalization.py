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
                luminance_histogram_equalization,
                monochrome_histogram_equalization
                )


img = cv2.imread('./images/scene.png')
# cv2.imshow('Original Image', img)
# cv2.waitKey(0)
img = resize(img, 0.4)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

equalized_img = luminance_histogram_equalization(img)
equalized_gray = monochrome_histogram_equalization(gray_img)


# cv2.imshow('Equalized Luminisence Image', equalized_img)
# cv2.imshow('Equalized Gray Image', equalized_gray)
# cv2.waitKey(0)


# Initialize subplot grid
fig, axes = initialize_subplot_grid(n_rows=2, n_cols=2, figsize=(15, 7))

## ~~ Luiminiace Histogram Equalization ~~
# Plot histograms
plot_bgr_histogram(axes[0, 0], img, 'Original Image Histogram')
plot_bgr_histogram(axes[0, 1], equalized_img, 'Equalized Image Histogram')

# Plot images
plot_img(axes[1, 0], img, "Original Image")
plot_img(axes[1, 1], equalized_img, "Equalized")

## ~~ Monochrome Histogram Equalization ~~
# plot_monochrome_histogram(axes[0, 0], gray_img, 'Original Image Histogram')
# plot_monochrome_histogram(axes[0, 1], equalized_gray, 'Equalized Histogram')

# plot_img(axes[1, 0], gray_img, "Original Image")
# plot_img(axes[1, 1], equalized_gray, "Equalized")

plt.tight_layout()
plt.show()
