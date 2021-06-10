import numpy as np
import cv2

# img = cv2.imread('lena.jpg', 1)
img=np.zeros([512, 512, 3],np.uint8)

img=cv2.line(img,(0,0),(255,255),(236,24,255),10)
img=cv2.arrowedLine(img,(10,50),(255,255),(0,24,255),10)

img=cv2.rectangle(img,(384,0),(510,128),(0,255,0),-1) #fill shape provide -1 as a thickness
img=cv2.circle(img,(384,234),68,(234,255,50),-1)
font=cv2.FONT_HERSHEY_DUPLEX
img=cv2.putText(img,'Opencv',(10,500), font,4,(0,255,255),10,cv2.LINE_AA)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindow()