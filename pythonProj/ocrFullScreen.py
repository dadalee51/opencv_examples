#ocr
import cv2
import pytesseract
import time

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    cv2.imshow('myimg', img)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print("image read:"+pytesseract.image_to_string(img2, lang='eng', config='-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'))
    c = cv2.waitKey(1)
    if c == 27:
        break
cap.release()
cv2.destroyAllWindows()