import cv2
import matplotlib.pyplot as plt
import numpy as nu

# channel 0 corresponds to the only camera attached to the computer
cap = cv2.VideoCapture(0)

while(True):
    # ret is boolean (True/False) and tells whether frame was read correctly or not
    # frame has the frame that was read
    ret, frame = cap.read()

    # the operation that we need to do    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # show the output on the screen
    cv2.imshow("webcam", gray)

    # keep doing so until key 'q' is pressed
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

# release the camera
cap.release()

# close all GUI windows
cv2.destroyAllWindows()
