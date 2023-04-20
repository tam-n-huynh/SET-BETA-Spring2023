import cv2

cap = cv2.VideoCapture(cv2.CAP_V4L2)

# Capture frame
ret, frame = cap.read()
if ret:
    cv2.imwrite('image.jpg', frame)

cap.release()
