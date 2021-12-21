import spidev
import RPi.GPIO as GPIO
import time
LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 100000
def analog_read(channel):
    # [byte_1, byte_2, byte_3]
    # byte_1 : 1
    # byte_2 : channel config, 1000 0000 : channel 0
    # byte_3 : 0(ignored)
    ret = spi.xfer2([1, (8+channel) << 4, 0])
    adc_out = ((ret[1] & 3)<< 8) + ret[2]
    return adc_out
try:
    while True:
        ldr_value = analog_read(0)
        print("LDR Value : %d" %ldr_value)
        time.sleep(0.1)
        if ldr_value<512:
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.1)
finally:
    spi.close()