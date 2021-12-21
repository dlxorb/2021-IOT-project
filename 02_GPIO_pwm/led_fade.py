import RPi.GPIO as GPIO
import time

LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

#PWM인스턴스 생성, 주파수 설정, 1초에 50번
pwm = GPIO.PWM(LED_PIN, 50)
pwm.start(0) #duty cycle (0~100)
try:
    for j in range(3):
        #서서히 켜짐(0~100)
        for i in range(0, 101, 5):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.1) 
        #서서히 꺼짐(100~0)
        for i in range(100, 1, -5):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.1)
finally:
    pwm.stop()
    GPIO.cleanup()
    print('cleanup and exit')
        