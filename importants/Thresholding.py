# syntax: thresholded=cv2.threshold(image,thresh_value,max_value,method)
#thres value=(0-255),max value=255,method=cv2.THRESH_BINARY
"""
here thresh value is 150, so if any value is 90->turns completely black
if 180->completely white
""" 

import cv2
img=cv2.imread("flower.png",cv2.IMREAD_GRAYSCALE)
ret,thresholded=cv2.threshold(img,150,255,cv2.THRESH_BINARY)
cv2.imshow("Original image",img)
cv2.imshow("Threshold image",thresholded)
cv2.waitKey(0)
cv2.destroyAllWindows()