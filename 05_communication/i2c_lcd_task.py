from lcd import drivers
import time
import datetime
import Adafruit_DHT

display = drivers.Lcd()

sensor = Adafruit_DHT.DHT11
DHT_PIN = 4

try:
  print("Writing to display")
  while True:
    now = datetime.datetime.now()
    h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
    
    display.lcd_display_string(now.strftime("%x%X"), 1)
    
    if h is not None and t is not None:
      display.lcd_display_string("%.1f*, %.1f%%" % (t, h), 2)
    else:
      display.lcd_display_string("read error", 2)

finally:
  display.lcd_clear()
  print("cleaning up!")