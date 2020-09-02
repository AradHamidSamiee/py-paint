import numpy as np
import cv2
import urllib.request
import matplotlib.pyplot as plt
print("OpenCV-Python Version %s" % cv2.__version__)

# Create a black image
img = np.zeros((512,512, 3), np.uint8) # numpy.zeros : creates an array filled with zeros (black)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,200),(255,511),(0,0,255),5)
img = cv2.line(img,(255,511),(511,200),(0,0,255),5)
img = cv2.line(img,(511,200),(360,0),(0,0,255),5)
img = cv2.line(img,(360,0),(255,160),(0,0,255),5)
img = cv2.line(img,(255,160),(155,0),(0,0,255),5)
img = cv2.line(img,(155,0),(0,200),(0,0,255),5)

# Drawing Rectangle
img = cv2.rectangle(img,(170,170),(340,340),(0,255,0),10)

# Drawing Circle
img = cv2.circle(img,(255,255), 75, (255,255,0), -1)

# Drawing Ellipse
# img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# Drawing Polygon
pts = np.array([[0,200],[255,511],[511,200],[360,0],[255,160],[155,0]], np.int32)
img = cv2.polylines(img,[pts],True,(255,0,0), 2)

# Adding Text to Images
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'I Love',(80,110), font, 4,(255,255,255),2,cv2.LINE_AA)
cv2.putText(img,'OpenCV',(196,265), font, 1,(255,255,255),2,cv2.LINE_AA)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
