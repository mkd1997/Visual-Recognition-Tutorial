import cv2
import matplotlib.pyplot as plt
import numpy as nu

# channel 0 corresponds to the only camera attached to the computer
cap = cv2.VideoCapture(0)

while(True):
    # ret is boolean (True/False) and tells whether frame was read correctly or not
    # frame has the frame that was read
    ret, frame = cap.read()

    # convert the image to grayscale
    # apply bilateral filtering to remove noise (this is necessary)
    # apply canny edge detection
    # find and fill the contours
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gray_filtered = cv2.bilateralFilter(gray, 7, 50, 50)
    edges = cv2.Canny(gray, 10, 30)    
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour_img = cv2.drawContours(frame.copy(), contours, -1, (255,0,0), thickness=-1)

    # show the output on the screen
    cv2.imshow("output", contour_img)

    # keep doing so until key 'q' is pressed
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

# release the camera
cap.release()

# close all GUI windows
cv2.destroyAllWindows()
