import cv2
import numpy

# temp? have to see if it's needed
from djitellopy import Tello

def detect():
    # sets the color requirement to detect
    # it will detect the color red
    lower = numpy.array([0, 150, 20])
    upper = numpy.array([15, 255, 255])

    # temp: must be replaced with connect.py (or something like that)
    drone = Tello()
    drone.connect()

    #turns drone's camera on
    drone.streamon()
    frame_read = drone.get_frame_read()

    while True:
        img = frame_read.frame
        image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(image, lower, upper)

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # check if it detects something
        if len(contours) != 0:
            for contour in contours:
                if cv2.contourArea(contour) > 500:
                    # when it detects it draws a line around the object
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(img, (x,y), (x + w, y + h), (0, 0, 255), 3)

                    # replace with something else
                    drone.flip_back()
                    drone.land()

        # shows what the drone sees on screen
        cv2.imshow("mask", mask)
        cv2.imshow("drone", img)
        cv2.waitKey(1)
