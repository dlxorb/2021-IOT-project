import picamera
import time
path = '/home/pi/src4/06_multimedia'
camera = picamera.PiCamera()
try:
    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(3)
    while True:
        now_str = time.strftime("%Y%m%d_%H%M%S")
        cmd = input("photo:1, video:2, exit:9 >")
        if cmd=='1':
            camera.capture('%s/photo_%s.jpg' % (path, now_str))
        elif cmd=='2':
            camera.start_recording('%s/video_%s.h264' % (path, now_str))
            input('press enter to stop')
            camera.stop_recording()
        elif cmd=='9':
            break
        else:
            print("incorrect command")
finally:
    camera.stop_preview()


