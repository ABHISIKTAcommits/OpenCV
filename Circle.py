import cv2
image=cv2.imread("ganesha.jpg")
if image is None:
    print("Cannot load image")
else:
    print ("image is loaded")
    # cv2.circle(image,center,radius,color,circle width)
    # to fill circle, circle width is -1
    cv2.circle(image,(150,150),100,(255,100,200),13)
    cv2.imshow("Circle Drawing Image",image) # Original Image is overwritten so no need to print
    cv2.waitKey(0)
    cv2.destroyAllWindows()
