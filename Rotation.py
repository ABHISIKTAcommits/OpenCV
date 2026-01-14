import cv2
image=cv2.imread("ganesha.jpg")
if image is None:
    print("Cannot load image")
else:
    print ("image is loaded")
    (h,w)=image.shape[:2] #channels bgr is ignored here
    center=(w//2,h//2) # // -> integer division
    M =cv2.getRotationMatrix2D(center,90,1.0) # scale factor 1 -> original size, 1.5 -> zoom in, 0.5 -> zoom out
    rotated=cv2.warpAffine(image,M,(w,h))
    cv2.imshow("Original image",image)
    cv2.imshow("Rotated image",rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
