import numpy as np
import cv2
from matplotlib import pyplot as plt
cap1 = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(2)

stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
while True:
	_, imgL = cap1.read()
	_, imgR = cap2.read()
	imgL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
	imgR = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)
	disparity = stereo.compute(imgL,imgR)
	cv2.imshow("1", imgL)
	cv2.imshow("2", imgR)
	#plt.imshow(disparity,'gray')
	#plt.show()
	if cv2.waitKey(1)==27:
		break
		
cap1.release()
cap2.release()
cv2.destroyAllWindows()