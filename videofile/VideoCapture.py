# cap=cv2.VideoCapture(source) 
# Source is 0 for inbuilt cam
# Source is 1 for external cam

import cv2
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# start cam, dshow is direct show
while True:
    ret,frame = cap.read() # read images of vdo frame by frame
    if not ret:
        print("Couldnt read frame")
        break
    cv2.imshow("Webcam Feed ",frame) # display
    # 0xFF is bitwise AND operation here if check if 113&113 -> 113=113 then enter loop
    if cv2.waitKey(40) & 0xFF == ord('q'): # ord finds ascii of q =113
# wait 1ms, check user press anything.
# if user press 'q' exit loop
        print("Quitting...")
        break
cap.release() #stop cam
cv2.destroyAllWindows()