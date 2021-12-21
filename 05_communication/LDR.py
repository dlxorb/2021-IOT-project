import spidev
import time
#SPI 인스턴스 생성
spi = spidev.SpiDev()
#SPI 통신 시작
spi.open(0,0) #bus, dev
#속도 설정
spi.max_speed_hz = 1000000
#데이터 읽기
def analog_read(channel) :
    spi.xfer2([1, (8 + channel) << 4, 0])
    print(ret)
    adc_out = ((ret[1] & 3) <<8) +ret[2]
    return adc_out

try:
    while True:
        reading = analog_read(0) #reading(0_1023)
        print("Reading=%d" %reading)
        time.sleep(0.5)
finally:
    spi.close()