import cv2
import numpy as np

img = cv2.imread('images/skull.png', 0)
#Resize Image
scale_percent = 50
w = int(img.shape[1] * scale_percent/100)
h = int(img.shape[0] * scale_percent/100)
new_dims = (w, h)
img = cv2.resize(img, new_dims, interpolation=cv2.INTER_LINEAR)

# Grey Level Scaling
lower_threshold = 150
upper_threshold = 200

scaled = img


r = cv2.hconcat([img, scaled])
cv2.imshow('win', r)
cv2.waitKey(0)
cv2.waitKey(0)

