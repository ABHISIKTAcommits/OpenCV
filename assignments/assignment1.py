import cv2
loc=input("enter image path: ")
image=cv2.imread(loc)
if image is not None:
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    print("Press 1 to show image \n Press 2 to save image")
    choice=input("\n Enter your choice: ")
    if choice == "1":
        cv2.imshow("Ganesh Grey",gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif choice == "2":
        name=input("Enter the output name of image to save: ")
        cv2.imwrite(name,gray)
else:
    print("couldnt load image")