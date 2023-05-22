import cv2
import matplotlib.pyplot as plt
import numpy as np

large_img = cv2.imread('image\street.jpg')
watermakr = cv2.imread('image\cola2.jpg')

print("large_image size >> ", large_img.shape)
print("watermakr image size >> ", watermakr.shape)

img1 = cv2.resize(large_img, (800, 600))
img2 = cv2.resize(watermakr, (800, 600))

print("img1 reize >>", img1.shape)
print("img2 reize >>", img2.shape)

blended = cv2.addWeighted(img1, 1, img2, 1, 0)
cv2.imshow("image show", blended)
cv2.waitKey(0)
