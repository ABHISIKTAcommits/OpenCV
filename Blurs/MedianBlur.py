import cv2
image =cv2.imread("BLUR2.png")
blur=cv2.medianBlur(image,15)
cv2.imshow("Original Image",image)
cv2.imshow("Clean Image",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()