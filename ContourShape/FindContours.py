# contour: finding boundary of any shape by points or lines
# syntax: contours,hierarchy=cv2.findContours(image,mode,method)
# image -> binary, mode-> 1. How many contours 2. what kind of contours
# mode-> 1. RETR_TREE= internal+ext+hierarchy, 2. create_external=outermost shapes,retr_list=internal+ext(without hierarchy)
# contour = return as list, hierarchy = relation b/w contour
import cv2

img = cv2.imread("flower.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 150)

contours, hierarchy = cv2.findContours(
    edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

cv2.imshow("Edges", edges)
cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# syntax: cv2.drawContours(image,contours,contour_index,color,thickness)
