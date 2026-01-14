"""
1. download files from https://github.com/opencv/opencv/tree/master/data/haarcascades
2. detectMultiScale() -> scan & detect faces
   1.1 -> balance, not too slow or fast
   5   -> minNeighbours
"""
import cv2

face_cascade = cv2.CascadeClassifier(
    r"C:\Users\ABHISIKTA\OneDrive\Desktop\OpenCv\githubfiles\haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Webcam Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
"""
x -> how far from left
y -> how far from top
w -> width of face
h -> height of face
"""