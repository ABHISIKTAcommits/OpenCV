# syntax: edges=cv2.Canny(image, threshold1,threshold2)
# uses: detect borders,separate objects,feature extraction
# threshold1=threshold value over which any value goes make it completely white 
# threshold2=threshold value lower than which any value goes make it completely dark 

import cv2
img=cv2.imread("flower.png",cv2.IMREAD_GRAYSCALE)
edges=cv2.Canny(img,50,150)
cv2.imshow("Original image",img)
cv2.imshow("Edges extracted image",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()