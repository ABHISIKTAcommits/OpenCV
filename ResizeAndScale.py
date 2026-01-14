import cv2
image=cv2.imread("ganesha.jpg")
if image is None:
    print("Cannot load image")
else:
    print ("image is loaded")
    resize=cv2.resize(image,(300,300))
    cv2.imshow("Original image",image)
    cv2.imshow("Resized image",resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
