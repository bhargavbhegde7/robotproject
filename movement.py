import cv2
import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1A = 18
Motor2A = 16
Motor3A = 22

Motor1B = 23
Motor2B = 21
Motor3B = 19
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor3A,GPIO.OUT)

GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor3B,GPIO.OUT)
 
ck=1
while ck==1:
	ch = input()
 
	if ch == 1:
		print "FORWARD MOTION"
		GPIO.output(Motor1A,GPIO.HIGH)
		GPIO.output(Motor2A,GPIO.LOW)
		GPIO.output(Motor3A,GPIO.HIGH)		
		GPIO.output(Motor1B,GPIO.HIGH)
		GPIO.output(Motor2B,GPIO.LOW)
		GPIO.output(Motor3B,GPIO.HIGH)
 
	if ch == 2:
		print "BACKWARD MOTION"
		GPIO.output(Motor1A,GPIO.LOW)
		GPIO.output(Motor2A,GPIO.HIGH)
		GPIO.output(Motor3A,GPIO.HIGH)		
		GPIO.output(Motor1B,GPIO.LOW)
		GPIO.output(Motor2B,GPIO.HIGH)
		GPIO.output(Motor3B,GPIO.HIGH)
 
	if ch == 3:
		print "STOP"
		GPIO.output(Motor3A,GPIO.LOW)
		GPIO.output(Motor3B,GPIO.LOW)
 
	if ch == 4:
		print "FINISHED"
		ck=4
		GPIO.cleanup()

