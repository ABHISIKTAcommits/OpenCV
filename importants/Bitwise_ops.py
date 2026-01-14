"""
1- cv2.bitwise_and(img1,img2) -> Keeps only the common white part
2- cv2.bitwise_or(img1,img2) -> Combines both shape
3- cv2.bitwise_not(img1) -> Reverses colors

1. img1,2 height width should be same
2. use only black and white
"""
import cv2
import numpy as np
img1=np.zeros((300,300),dtype="uint8")
img2=np.zeros((300,300),dtype="uint8")
"""
Creates black images of size 300 × 300 pixels
zeros → fills the image with 0=black color
uint8 → pixel values from 0 to 255
"""
cv2.circle(img1,(150,150),100,255,-1)
"""
img1 → where to draw
(150,150) → center of the circle
100 → radius
255 → white color
-1 → fill the circle completely
Result: A solid white circle in the middle of a black image.
"""
cv2.rectangle(img2,(100,100),(250,250),255,-1)
bitwise_and=cv2.bitwise_and(img1,img2)
bitwise_or=cv2.bitwise_or(img1,img2)
bitwise_not=cv2.bitwise_not(img1)
cv2.imshow("Circle",img1)
cv2.imshow("Rectangle",img2)
cv2.imshow("AND",bitwise_and)
cv2.imshow("OR",bitwise_or)
cv2.imshow("NOT",bitwise_not)
cv2.waitKey(0)
cv2.destroyAllWindows()