import RPi.GPIO as GPIO
import time
BUZZER_PIN = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(10)

melody1 = [392, 392, 440, 440, 392, 392, 330]
melody2 = [392, 392, 330, 330, 294]
melody3 = [392, 330, 294, 330, 262]

try:
    for i in melody1:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(0.5)
    for i in melody2:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(1)
    for i in melody1:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(0.5)
    for i in melody3:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
finally:
    pwm.stop()
    GPIO.cleanup()
    

