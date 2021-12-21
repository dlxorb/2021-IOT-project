import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Camera open failed')
    exit()
#fourcc(four character code)
#KIVX(avi), MP4V(mp4), X264(h264)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(frame, 50, 100)
    cv2.imshow('frame1', gray)
    cv2.imshow('frame2', frame)
    cv2.imshow('frame3', edge)
   # out.write(frame)
    # 1000=1초, 20=0.01초
    if cv2.waitKey(10) == 13:
        break
cap.release()
cv2.destroyAllWindows()
