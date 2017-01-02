import cv2
import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1 = 16
Motor2 = 18
Motor3 = 22
 
GPIO.setup(Motor1,GPIO.OUT)
GPIO.setup(Motor2,GPIO.OUT)
GPIO.setup(Motor3,GPIO.OUT)
 
ck=1
while ck==1:
    ch = input()
 
    if ch == 1:
        print "FORWARD MOTION"
        GPIO.output(Motor1,GPIO.HIGH)
        GPIO.output(Motor2,GPIO.LOW)
        GPIO.output(Motor3,GPIO.HIGH)
 
    if ch == 2:
        print "BACKWARD MOTION"
        GPIO.output(Motor1,GPIO.LOW)
        GPIO.output(Motor2,GPIO.HIGH)
        GPIO.output(Motor3,GPIO.HIGH)
 
    if ch == 3:
        print "STOP"
        GPIO.output(Motor3,GPIO.LOW)
 
    if ch == 4:
        print "FINISHED"
        ck=4
        GPIO.cleanup()
