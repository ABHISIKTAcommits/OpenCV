import cv2
image=cv2.imread("ganesha.jpg")
if image is None:
    print("Cannot load image")
else:
    print ("image is loaded")
    crop=image[100:600,50:250]
    cv2.imshow("Original image",image)
    cv2.imshow("Cropped image",crop)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
