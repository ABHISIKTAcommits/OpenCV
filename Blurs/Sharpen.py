import cv2
import numpy as np
image=cv2.imread("BLUR2.png")
sharpen_kernel=np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])
sharpened=cv2.filter2D(image,-1,sharpen_kernel)
cv2.imshow("Original Image",image)
cv2.imshow("Clean Image",sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()