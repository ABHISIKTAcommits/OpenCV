import cv2
image=cv2.imread("ganesha.jpg")
if image is None:
    print("Cannot load image")
else:
    print ("image is loaded")
    # cv2.putText(image,text,org -> bottom left corner of text,font,fontScale -> 1.0=normal 2.0=big, color,thickness)
    cv2.putText(image,"This idol is made by Abhisikta",(700,80),
                cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1.2,(155,100,150),2)
    cv2.imshow("Text On Image",image) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
