import cv2
import os

cap = cv2.VideoCapture("phw.mp4")
index = 1

while(cap.isOpened()):
    ret, frame = cap.read()
    # defaultpath = "/wyh/"
    # filename = str(index) + ".jpg"
    # file = os.path.join(defaultpath,filename)
    # print(file)
    cv2.imwrite(str(index)+'.jpg',frame)

    if ret == False or index == 60:
        break
    index += 1

cap.release()
cv2.destroyAllWindows()
