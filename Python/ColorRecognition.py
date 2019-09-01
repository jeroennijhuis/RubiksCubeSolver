#necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

#initialize the camera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(1)
 
# continuously capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array
	time.sleep(0.3)
	
	#Pixel settings for drawing cubes
	startingWidth = 280
	startingHeight = 170
	cubesize = 30
	cubeMargin = 80

	for x in range(0, 3): 
		width = startingWidth + x * (cubesize + cubeMargin)
		for y in range(0, 3): 
			height = startingHeight + y*(cubesize + cubeMargin)
			blue, green, red = image[height + 15, width + 15]
			cv2.rectangle(image,(x*cubesize ,y*cubesize),((x*cubesize) + cubesize, (y*cubesize) + cubesize), (255,255,255), 2) 	
			
			#red
			if red > 100 and green < 56 and blue > 17 and blue < 90 :
				cv2.rectangle(image,(x*cubesize ,y*cubesize),((x+1)*cubesize, (y+1)*cubesize), (0,0,255), -1) 
			
			#yellow
			elif red > 208 and green > 200 and blue < 62 : 
				cv2.rectangle(image,(x*cubesize ,y*cubesize),((x+1)*cubesize, (y+1)*cubesize), (0,255,255), -1) 
			
			#green
			elif red < 130 and green > 80 and green < 256 and blue < 83 : 
				cv2.rectangle(image,(x*cubesize ,y*cubesize),((x+1)*cubesize, (y+1)*cubesize), (0,255,0), -1) 
				
			#blue
			elif red < 100 and green > 30 and green < 120 and blue > 50: 
				cv2.rectangle(image,(x*cubesize ,y*cubesize),((x+1)*cubesize, (y+1)*cubesize), (255,0,0), -1) 

			#orange	
			elif red > 180 and green > 100 and green < 200 and blue < 80 : 
				cv2.rectangle(image,(x*cubesize ,y*cubesize),((x+1)*cubesize, (y+1)*cubesize), (0,140,255), -1) 
				print image[height + 15, width + 15]
			
			#white
			elif red > 150 and green > 150 and blue > 80 :
				cv2.rectangle(image,(x*cubesize ,y*cubesize),((x+1)*cubesize, (y+1)*cubesize), (255,255,255), -1) 
				
			else :
				cv2.rectangle(image,(width ,height),(width + cubesize,height + cubesize), (255,255,255), 2) 	
				print (red, green, blue)
				
	cv2.imshow("Rubiks Cube", image)
	cv2.waitKey(1) & 0xFF
	rawCapture.truncate(0)
	
