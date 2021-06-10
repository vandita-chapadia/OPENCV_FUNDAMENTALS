import cv2
import numpy as np
img=cv2.imread('lena.jpg')
lr1=cv2.pyrDown(img)
lr2=cv2.pyrDown(lr1)

hr2=cv2.pyrUp(lr2)
cv2.imshow('Original Image',img)
cv2.imshow('prDown 1 image',lr1)
cv2.imshow('prDown 2 image',lr2)
cv2.imshow('prUp 2 image',hr2)
cv2.waitKey(0)
cv2.destroyAllWindows()