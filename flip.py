import cv2
image=cv2.imread("ganesha.jpg")
if image is None:
    print("Cannot load image")
else:
    print ("image is loaded")
    flip_h=cv2.flip(image,1)
    flip_v=cv2.flip(image,0)
    flip_both=cv2.flip(image,-1)
    cv2.imshow("Original image",image)
    cv2.imshow("Horizontal Flipped image",flip_h)
    cv2.imshow("Vertical Flipped image",flip_v)
    cv2.imshow("Both Side Flipped image",flip_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
