import cv2
#read image
image=cv2.imread("ganesha.jpg",-1)
if image is None:
    print("000")
else:
    print("woahh")
#display iamge
cv2.imshow("Ganesh Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#edit and save image
if image is not None:
    success=cv2.imwrite("newganesha.jpg",image)
    if success:
        print("image saved successfully as 'newganesha.jpg'")
    else:
        print("failed to save image")
else:
    print("couldnt load image")
