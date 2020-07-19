import cv2
 
cap = cv2.VideoCapture(0)
 
# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")
 
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.circle(frame,(50,50), 63, (0,0,255), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'TIGO',(10,200), font, 4,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow('Input', frame)
 
    c = cv2.waitKey(1)
    if c == 27:
        break
 
cap.release()
cv2.destroyAllWindows()