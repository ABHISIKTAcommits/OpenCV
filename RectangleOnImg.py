import cv2
image=cv2.imread("ganesha.jpg")
if image is None:
    print("Cannot load image")
else:
    print ("image is loaded")
    #pt1 is top left corner of rectangle (x1,y1)
    #pt2 is bottom right corner of rectangle (x2,y2)
    pt1=(150,150) # (x1,y1)
    pt2=(350,400) # (x2,y2)
    color=(255,150,240)
    thick=8
    cv2.rectangle(image,pt1,pt2,color,thick)
    cv2.imshow("Rectangle Drawing Image",image) # Original Image is overwritten so no need to print
    cv2.waitKey(0)
    cv2.destroyAllWindows()
