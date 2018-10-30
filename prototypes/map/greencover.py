import cv2
from urllib.request import urlopen
from PIL import Image
import numpy as np

## Read

img = cv2.imread('featured_3.jpg')

## convert to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

## mask of green (36,0,0) ~ (70, 255,255)
mask1 = cv2.inRange(hsv, (36,0,0), (86 ,255 ,255))#(70, 255,255))
cv2.imwrite("threshold.png", mask1)

imask = mask1>0
green = np.zeros_like(img, np.uint8)
green[imask] = img[imask]

## save
cv2.imwrite("green.png", green)
print(np.count_nonzero(mask1))
print(mask1.size)
print("Percent : ", np.count_nonzero(mask1)/mask1.size * 100)
