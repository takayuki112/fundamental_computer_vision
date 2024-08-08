import cv2
import numpy as np

img = cv2.imread('images/skull.png', 0)
#Resize Image
scale_percent = 50
w = int(img.shape[1] * scale_percent/100)
h = int(img.shape[0] * scale_percent/100)
new_dims = (w, h)
img = cv2.resize(img, new_dims, interpolation=cv2.INTER_LINEAR)

#Contrast Stretching
lower_threshold = 150
lower_value = 20
upper_threshold = 220
upper_value = 240

# Compute the scaling factors
slope = (upper_value - lower_value) / (upper_threshold - lower_threshold)
intercept = lower_value - slope * lower_threshold

stretched_img = np.clip(slope * img + intercept, 0, 255).astype(np.uint8)


r = cv2.hconcat([img, stretched_img])
cv2.imshow('win', r)
cv2.waitKey(0)
cv2.waitKey(0)

