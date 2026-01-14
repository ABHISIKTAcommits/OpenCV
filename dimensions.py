import cv2
image=cv2.imread("ganesha.jpg",-1)
if image is not None:
    h,w,c=image.shape
    print(f"Image loaded:\nHeight: {h}\nWidth: {w}\nChannels: {c}")
else:
    print("cant load image")