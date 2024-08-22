import numpy as np
import cv2

from utils.image import resize, adaptive_histogram_equalization

img = cv2.imread('./images/scene.png', 0)
img = resize(img, 0.4)

equalized = adaptive_histogram_equalization(img)

cv2.imshow('Original Image', img)
cv2.imshow('Equalized Image', equalized)

cv2.waitKey(0)
cv2.destroyAllWindows()

