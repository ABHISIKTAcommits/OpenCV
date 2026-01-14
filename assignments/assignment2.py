import cv2
loc=input("enter image path: ")
image=cv2.imread(loc)
if image is None:
    print("No image is found!")
else:
    while True:
        print("\n1. Insert Line")
        print("2. Insert Circle")
        print("3. Insert Rectangle")
        print("4. Insert Text")
        print("5. End Code")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            print ("Image is loaded. Line is being inserted..")
            img1 = image.copy()
            pt1=(50,100)
            pt2=(300,100) 
            color=(255,0,0)
            thick=8
            cv2.line(img1,pt1,pt2,color,thick)
            cv2.imshow("Line Drawing Image",img1) 
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            choice=input("Do you want to save the new image? (Y/N): ")
            if choice.upper() == 'Y':
                if image is not None:
                    success=cv2.imwrite("newganeshal.jpg",img1)
                    if success:
                        print("image saved successfully as 'newganeshal.jpg'")
                    else:
                        print("failed to save image")
            else:
                continue

        elif ch == 2:
            print ("image is loaded. circle is being inserted..")
            img2 = image.copy()
            cv2.circle(img2,(150,150),100,(255,100,200),13)
            cv2.imshow("Circle Drawing Image",img2)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            choice=input("Do you want to save the new image? (Y/N): ")
            if choice.upper() == 'Y':
                if image is not None:
                    success=cv2.imwrite("newganeshac.jpg",img2)
                    if success:
                        print("image saved successfully as 'newganeshac.jpg'")
                    else:
                        print("failed to save image")
            else:
                continue

        elif ch ==3:
            print ("image is loaded. Rectangle is being inserted..")
            img3 = image.copy()
            pt1=(150,150)
            pt2=(350,400)
            color=(255,150,240)
            thick=8
            cv2.rectangle(img3,pt1,pt2,color,thick)
            cv2.imshow("Rectangle Drawing Image",img3)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            choice=input("Do you want to save the new image? (Y/N): ")
            if choice.upper() == 'Y':
                if image is not None:
                    success=cv2.imwrite("newganeshar.jpg",img3)
                    if success:
                        print("image saved successfully as 'newganeshar.jpg'")
                    else:
                        print("failed to save image")
            else:
                continue

        elif ch ==4:
            print ("image is loaded. Text is being inserted..")
            img4 = image.copy()
            cv2.putText(img4,"This idol is made by Abhisikta"
                        ,(700,80),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1.2,(155,100,150),2)
            cv2.imshow("Text On Image",img4) 
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            choice=input("Do you want to save the new image? (Y/N): ")
            if choice.upper() == 'Y':
                if image is not None:
                    success=cv2.imwrite("newganeshat.jpg",img4)
                    if success:
                        print("image saved successfully as 'newganeshat.jpg'")
                    else:
                        print("failed to save image")
            else:
                continue

        elif ch ==5:
            print("Program ended!")
            break
