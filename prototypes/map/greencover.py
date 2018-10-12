import cv2
from urllib.request import urlopen
from PIL import Image
import numpy as np

## Read
img = cv2.imread('featured_3.jpg')

## convert to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

## mask of green (36,0,0) ~ (70, 255,255)
mask1 = cv2.inRange(hsv, (36, 0, 0), (70, 255,255))
cv2.imwrite("threshold.png", mask1)

'''
img = Image.open(urlopen('https://maps.googleapis.com/maps/api/staticmap?center=40.714728,-73.998672&zoom=16&size=600x300&maptype=satellite&key=AIzaSyDRjavHrEvei0wuHLRYUEbEtRH3YMGcKpQ'))
img = np.array(img)


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)

cv2.imwrite("target.png", mask1)
'''