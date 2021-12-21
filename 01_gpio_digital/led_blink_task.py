import RPi.GPIO as GPIO
import time
GREEN = 7
YELLOW = 8
RED = 9
GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)
GPIO.output(RED, GPIO.HIGH)
print("RED ON")
time.sleep(2)
GPIO.output(RED, GPIO.LOW)
GPIO.output(YELLOW, GPIO.HIGH)
print("YELLOW ON")
time.sleep(2)
GPIO.output(YELLOW, GPIO.LOW)
GPIO.output(GREEN, GPIO.HIGH)
print("GREEN ON")
time.sleep(2)
GPIO.output(GREEN, GPIO.LOW)
GPIO.cleanup()