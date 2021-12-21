import spidev
import time
#SPI 인스턴스 생성
spi = spidev.SpiDev()
#spi 통신시작
spi.open(0, 0)
#SPI 통신 속도 설정
spi.max_speed_hz = 100000
#0~7까지의 8개의 채널에서 SPI 데이터 읽기
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
        reading = analog_read(0)
        #접압수치로 변환
        voltage = reading * 3.3 / 1023
        print("Reading=%d, Voltage=%f" %(reading, voltage))
        time.sleep(0.1)
finally:
    spi.close()