import cv2
import numpy as np

img = cv2.imread('images/scene.png', 0)
#Resize Image
scale_percent = 30
w = int(img.shape[1] * scale_percent/100)
h = int(img.shape[0] * scale_percent/100)
new_dims = (w, h)
img = cv2.resize(img, new_dims, interpolation=cv2.INTER_LINEAR)

#Power Tf
gamma = 1
c = 255
tf = c * (np.power(img/255, gamma))
tf = tf.astype(img.dtype)
print(img.dtype)

r = cv2.hconcat([img, tf])
cv2.imshow('win', r)
def on_change(value):
    gamma = value/100
    tf = c * (np.power(img, gamma))
    tf = tf.astype(img.dtype)
    r = cv2.hconcat([img, tf])
    cv2.imshow('win', r)
cv2.createTrackbar('slider', 'win', 0, 500, on_change)

cv2.waitKey(0)

