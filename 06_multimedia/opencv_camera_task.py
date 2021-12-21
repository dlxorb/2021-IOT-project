import cv2

cap = cv2.VideoCapture('output.avi')
if not cap.isOpened():
    print('Camera open failed')
    exit()
#fourcc(four character code)
#KIVX(avi), MP4V(mp4), X264(h264)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 30, (640, 480))
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('frame', frame)
    out.write(frame)
    # 1000=1초, 20=0.01초
    if cv2.waitKey(10) == 13:
        break
# ret, frame = cap.read()
# cv2.imwrite('output.jpg', frame)
cap.release()
out.release()
cv2.destroyAllWIndows()
