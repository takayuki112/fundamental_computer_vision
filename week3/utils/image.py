import cv2
import numpy as np

def resize(img, scale=0.5):
    w = int(scale * img.shape[1])
    h = int(scale * img.shape[0])
    return cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)

def luminance_histogram_equalization(img):
    yuv_image = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    yuv_image[:, :, 0] = cv2.equalizeHist(yuv_image[:, :, 0])
    eqed = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR)
    return eqed


def monochrome_histogram_equalization(img):
    return cv2.equalizeHist(img)
