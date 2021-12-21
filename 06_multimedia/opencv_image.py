import cv2

img=cv2.imread('end.jpg')
img2 = cv2.resize(img, (600, 400))

gray = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
edge1 = cv2.Canny(img, 50, 100)
edge2 = cv2.Canny(img, 100, 150)
edge3 = cv2.Canny(img, 150, 200)
#cv2.imshow('endgame', img)
#cv2.imshow('endgame2', img2)
#cv2.imshow('GRAY', gray)
cv2.imshow('edge1', edge1)
cv2.imshow('edge2', edge2)
cv2.imshow('edge3', edge3)
while True:
    if cv2.waitKey() == 13:
        break
cv2.imwrite('Endgame.jpg', gray)
cv2.destroyAllWIndows()