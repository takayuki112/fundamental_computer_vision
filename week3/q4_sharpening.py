import numpy as np
import cv2

img = cv2.imread('./images/scene.png')
img = cv2.resize(img, (0, 0), fx=0.4, fy=0.4)

sharpened = cv2.addWeighted(img, 2, cv2.GaussianBlur(img, (0, 0), sigmaX=1), -1, 0)

cv2.imshow('Original Image', img)
cv2.imshow('Sharpened Image', sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
