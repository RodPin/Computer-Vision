
import numpy as np
import cv2

##creating a black image
img = np.zeros((600,600,3))

##diagonal line through screen
cv2.line(img,(0,0),(599,599),(255,0,0))

## drawing rectangle
cv2.rectangle(img,(300,10),(200,300),(0,0,255))

##drawing circle
cv2.circle(img,(150,230),60,(255,210,30),10)

##creating a file that contains the new image
cv2.imwrite('teste.jpg',img)