import cv2
import numpy as np

I = cv2.imread('karimi.jpg',0)

tx = I.shape[0]
ty = 0

th =  90 # angle of rotation (degrees)
th *= np.pi / 180 # convert to radians

M = np.array([[np.cos(th),-np.sin(th),tx],
              [np.sin(th), np.cos(th),ty]])

J = cv2.warpAffine(I,M, (I.shape[0], I.shape[1]) )

cv2.imshow('I',I)
cv2.waitKey(0)

cv2.imshow('J',J)
cv2.waitKey(0)

