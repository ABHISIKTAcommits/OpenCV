import cv2
import time # used to pause so webcam can start properly

camera = cv2.VideoCapture(0) # 0→inbuilt laptop webcam 1→extUSB webcam

if not camera.isOpened():
    print("Camera not accessible")
    exit()

time.sleep(2)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID') #xvid is avi video format
recorder = cv2.VideoWriter("video1.avi", codec, 20, (frame_width, frame_height))
# params are: o/p file name, compression type,20fps,frame size
while True:
    success, image = camera.read()

    if not success:
        print("Frame not received")
        break

    recorder.write(image)
    cv2.imshow("Recording Live", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
recorder.release()
cv2.destroyAllWindows()
