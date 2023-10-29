import cv2 as cv

#Read Image Using OpenCV
img = cv.imread("Images/Lena.png")
cv.imshow("Lena",img)

cv.waitKey(0)
cv.closeAllWindows()
#Read Video Using OpenCV
frameWidht = 640
frameHeight = 360

cap = cv.VideoCapture("Resources/testVideo.mp4")
while True :
    success,img = cap.read()
    cv.imshow("Video",img)

#Press q close the video
    if cv.waitKey(0) & 0xFF == ord('q'):
        break

#Read Webcam Using OpenCV
frameWidht = 640
frameHeight = 480

cap = cv.VideoCapture(0) #0 is webcam port number
while True :
    success,img = cap.read()
    cv.imshow("Webcam",img)

#Press q close the video
    if cv.waitKey(0) & 0xFF == ord('q'):
        break
