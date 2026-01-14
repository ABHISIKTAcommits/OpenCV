import cv2
image =cv2.imread("ganesha.jpg")
blur=cv2.GaussianBlur(image,(7,7),3)
# params are: (image,(kernel_size_x,kernel_size_y),sigma)
#sigma is blur value, kernel size are always odd
cv2.imshow("Original Image",image)
cv2.imshow("Blurred Image",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()