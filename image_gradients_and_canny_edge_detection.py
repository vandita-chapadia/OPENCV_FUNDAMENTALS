import cv2
from matplotlib import pyplot as plt
import numpy as np


img=cv2.imread("sudoku.png",cv2.IMREAD_GRAYSCALE)
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap=np.uint(np.absolute(lap))
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1)
sobelx=np.uint8(np.absolute(sobelx))
sobely=np.uint8(np.absolute(sobely))
sobelCombined=cv2.bitwise_or(sobelx,sobely)

titles=['image','Laplacian','SobelX','SobelY','SobelCombine']
images=[img,lap,sobelx,sobely,sobelCombined]

for i in range(5):
    plt.subplot(3,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
