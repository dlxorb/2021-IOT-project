#도 음 출력하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(50)

melody = [262, 294, 330, 349, 392, 440, 494, 523]
BUZZER_PIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

try:
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(1)
finally:
    pwm.stop()
    GPIO.cleanup()

