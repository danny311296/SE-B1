import cv2
from urllib.request import urlopen
from PIL import Image
import numpy as np
from skimage import io
## Read

img = io.imread('https://maps.googleapis.com/maps/api/staticmap?center=40.714728,-73.998672&zoom=16&size=600x300&maptype=satellite&key=AIzaSyDRjavHrEvei0wuHLRYUEbEtRH3YMGcKpQ')
cv2.imwrite("satellite/input_map.png",img)
## convert to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imwrite("satellite/input_map_hsv.png",hsv)
## mask of green (36,0,0) ~ (70, 255,255)
mask1 = cv2.inRange(hsv, (36,0,0), (86 ,255 ,255))#(70, 255,255))
cv2.imwrite("satellite/map.png", mask1)

imask = mask1>0
green = np.zeros_like(img, np.uint8)
green[imask] = img[imask]

## save
cv2.imwrite("satellite/green.png", green)
print(np.count_nonzero(mask1))
print(mask1.size)
print("Percent : ", np.count_nonzero(mask1)/mask1.size * 100)
