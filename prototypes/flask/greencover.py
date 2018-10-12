import cv2
from urllib.request import urlopen
from PIL import Image
import numpy as np
from skimage import io
## Read

def get_image(lat,long):
    img = io.imread('https://maps.googleapis.com/maps/api/staticmap?center='+ str(lat)+','+str(long) + '&zoom=16&size=600x300&maptype=satellite&key=AIzaSyDRjavHrEvei0wuHLRYUEbEtRH3YMGcKpQ')
    #cv2.imwrite("satellite/input_map.png",img)
    return img
## convert to hsv
def convert_to_hsv(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #cv2.imwrite("satellite/input_map_hsv.png",hsv)
    return hsv

def green_mask(hsv):
## mask of green (36,0,0) ~ (70, 255,255)
    mask1 = cv2.inRange(hsv, (36,0,0), (86 ,255 ,255))#(70, 255,255))
    #cv2.imwrite("satellite/map.png", mask1)
    return mask1

def green_areas(img,mask):
    imask = mask>0
    green = np.zeros_like(img, np.uint8)
    green[imask] = img[imask]
    #cv2.imwrite("satellite/green.png", green)
    return green

def green_percent(mask):
    print(np.count_nonzero(mask))
    print(mask.size)
    print("Percent : ", np.count_nonzero(mask)/mask.size * 100)
    return np.count_nonzero(mask)/mask.size * 100

def green_index(lat,long):
    img = get_image(lat,long)
    hsv = convert_to_hsv(img)
    mask = green_mask(hsv)
    greenareas = green_areas(img,mask)
    return green_percent(mask)