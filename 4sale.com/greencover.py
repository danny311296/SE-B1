import cv2
import numpy as np
from skimage import io
import os

class Image_Processor:
    def __init__(self,lat,long):
        self.img = io.imread('https://maps.googleapis.com/maps/api/staticmap?center='+ str(lat)+','+str(long) + '&zoom=16&size=600x300&maptype=satellite&key=AIzaSyDRjavHrEvei0wuHLRYUEbEtRH3YMGcKpQ')
        self.hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        ## mask of green (36,0,0) ~ (70, 255,255)
        self.mask = cv2.inRange(self.hsv, (36,0,0), (86 ,255 ,255))
        imask = self.mask > 0
        green = np.zeros_like(self.img, np.uint8)
        green[imask] = self.img[imask]
        self.green = green
        self.green_percent = np.count_nonzero(self.mask)/self.mask.size * 100
        
    def store_images_for_pid(self,pid):
        if(not(os.path.isdir("static/images/properties/"+str(pid)))):
            os.mkdir("static/images/properties/"+str(pid))
        if(not(os.path.isdir("static/images/properties/"+str(pid)+"/greencover"))):
            os.mkdir("static/images/properties/"+str(pid)+"/greencover")
        cv2.imwrite("static/images/properties/"+str(pid)+"/greencover/input.png",self.img)
        cv2.imwrite("static/images/properties/"+str(pid)+"/greencover/hsv.png",self.hsv)
        cv2.imwrite("static/images/properties/"+str(pid)+"/greencover/mask.png",self.mask)
        cv2.imwrite("static/images/properties/"+str(pid)+"/greencover/green.png",self.green)