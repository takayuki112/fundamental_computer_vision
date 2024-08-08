import cv2
import numpy as np

img = cv2.imread('images/scene.png', 0)
#Resize Image
scale_percent = 20
w = int(img.shape[1] * scale_percent/100)
h = int(img.shape[0] * scale_percent/100)
new_dims = (w, h)
img = cv2.resize(img, new_dims, interpolation=cv2.INTER_LINEAR)

#Log Tf
c = 255 / (np.log(1 + np.max(img)))
tf = c * (np.log(img+1))
tf = tf.astype(img.dtype)

r = cv2.hconcat([img, tf])
cv2.imshow('win', r)
cv2.waitKey(0)

