import cv2
image=cv2.imread("ganesha.jpg")
if image is None:
    print("Cannot load image")
else:
    print ("image is loaded")
    pt1=(50,100) # (x1,y1)
    pt2=(300,100) # (x2,y2)
    color=(255,0,0)
    thick=8
    cv2.line(image,pt1,pt2,color,thick)
    cv2.imshow("Line Drawing Image",image) # Original Image is overwritten so no need to print
    cv2.waitKey(0)
    cv2.destroyAllWindows()
