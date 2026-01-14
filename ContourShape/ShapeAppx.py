# syntax: approx=cv2.approxPolyDP(contour,epsilon,True)
"""
epsilon= 0.01*cv2.arclength(contour,true)
smaller=more precise, more points
large= rougher, few points
"""
import cv2
import numpy as np

img1 = np.zeros((300,300), dtype="uint8")
cv2.circle(img1, (150,150), 100, 255, -1)

img = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)

_, thresh = cv2.threshold(img1, 120, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

for contour in contours:
    approx = cv2.approxPolyDP(
        contour, 0.01 * cv2.arcLength(contour, True), True
    )

    corners = len(approx)

    if corners == 3:
        shape = "Triangle"
    elif corners == 4:
        shape = "Rectangle"
    elif corners == 5:
        shape = "Pentagon"
    elif corners > 5:
        shape = "Circle"
    else:
        shape = "Unknown"

    cv2.drawContours(img, [approx], 0, (0,255,0), 2)

    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10
    cv2.putText(img, shape, (x,y),
                cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,0,0), 2)

cv2.imshow("Threshold", thresh)
cv2.imshow("Shape Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
