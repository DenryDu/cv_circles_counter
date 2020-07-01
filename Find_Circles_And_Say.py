
import cv2
import numpy as np

from espeakng import ESpeakNG

#init espeak object
import pyttsx3
engine = pyttsx3.init()

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imshow("",ret)
    # Our operations on the frame come here
    blur = cv2.medianBlur(frame, 5)
    gray = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
    image = gray

    #first layer of processing - to find the small circle
    circles1 = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,90,
                               param1=50, param2=28, minRadius=35, maxRadius=70)
    if circles1 is None:
        print("no circle")
        continue
        #exit()

    circles1 = np.uint16(np.around(circles1))

    #second layer of processing - to find the big circle
    circles2 = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,200,
                               param1=50, param2=60, minRadius=100, maxRadius=300)
    if circles2 is not None:
        circles2 = np.uint16(np.around(circles2))

        circles = np.append(circles1,circles2,axis=1)
        count =0
        for i in circles[0, :]:
             # draw the outer circle
             cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
             # draw the center of the circle
             cv2.circle(image,(i[0],i[1]),2,(0,0,255),3)
             count+=1
        cv2.imshow('detected circles',image)

        #print
        print("I found %i coins" % count)

        #read it out
        result="I found"+str(count)+"circles"
        print("I found %i circles" % count)
        engine.say(result)
        engine.runAndWait()

        #control the break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(0)
# import cv2
# import numpy as np
# #from espeakng import ESpeakNG
#
#
# img = cv2.imread("coin7.jpeg",0)
#
# img = cv2.medianBlur(img,5)
# outline = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
#
# circles1 = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,
#                            param1=50, param2=28, minRadius=35, maxRadius=70)
#
# circles1 = np.uint16(np.around(circles1))
#
# circles2= cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,200,
#                            param1=50, param2=60, minRadius=100, maxRadius=300)
# circles2 = np.uint16(np.around(circles2))
# circles = np.append(circles1,circles2,axis=1)
# count=0
# for i in circles[0, :]:
#      # draw the outer circle
#      cv2.circle(outline, (i[0], i[1]), i[2], (0, 255, 0), 2)
#      # draw the center of the circle
#      cv2.circle(outline,(i[0],i[1]),2,(0,0,255),3)
#      count+=1
#
# cv2.imshow('detected circles',outline)
# print("I found %i coins" % count)
# #esng = ESpeakNG()
# #esng.voice="chinese"
# #esng.say('你')
# cv2.waitKey(0)
