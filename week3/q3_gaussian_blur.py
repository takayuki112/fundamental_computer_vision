import numpy as np
import cv2

img = cv2.imread('./images/scene.png')
img = cv2.resize(img, (0, 0), fx=0.4, fy=0.4)  

blurred = cv2.GaussianBlur(img, (25, 25), sigmaX=1)

cv2.imshow('Original Image', img)
cv2.imshow('Blurred Image', blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()