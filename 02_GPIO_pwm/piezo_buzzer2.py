 #도 음 출력하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(50)

time.sleep(2)
pwm.ChangeDutyCycle(0)

pwm.stop()
GPIO.cleanup()