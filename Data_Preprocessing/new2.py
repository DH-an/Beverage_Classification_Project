import cv2
import numpy as np
import matplotlib.pylab as plt

# 이미지 읽기(img1 : 배경 이미지, img2 : 워터마크로 넣을 이미지)
# img2가 img1보다 작은 크기

cola = cv2.imread('image\cola.jpg',cv2.IMREAD_COLOR)
street = cv2.imread('image\street.jpg',cv2.IMREAD_COLOR)


h, w = cola.shape[:2]

print(h,w)

crop = street[0:h, 0:w]

cv2.copyTo(cola, crop)

cv2.imshow('street',street)