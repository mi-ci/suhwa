import cv2 as cv

a = 0
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("camera open failed")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Can't read camera")
        break

    cv.imshow('PC_camera', img)
    if cv.waitKey() == ord('c'):
        img_captured = cv.imwrite(f'img{a}.jpg', img)
        a = a + 1
    if cv.waitKey() == ord('q'):
        break

cap.release()
cv.destroyAllWindows()