import cv2
import numpy as np

img = cv2.imread('images/skull.png', 0)

#Resize Image
scale_percent = 60
w = int(img.shape[1] * scale_percent/100)
h = int(img.shape[0] * scale_percent/100)
new_dims = (w, h)
img = cv2.resize(img, new_dims, interpolation=cv2.INTER_LINEAR)

# Negative Tf
neg = np.max(img) - np.array(img)        # should this be max or 255
neg2 = 255 - np.array(img)

r = cv2.hconcat([img, neg, neg2])
cv2.imshow('win', r)
cv2.waitKey(0)

print("Max Intensity in original = ", np.max(img))
print("Some corresponding pixel values - ")
count = 10
for row in range(len(img)):
    for p in range(len(img[0])):
        print(img[row][p], "-->", neg[row][p])
        count -= 1
        if count < 0:
            exit()
