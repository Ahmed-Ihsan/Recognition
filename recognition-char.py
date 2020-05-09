import cv2
import pytesseract as tess

tess.pytesseract.tesseract_cmd=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
w =0
video_capture = cv2.VideoCapture(0)
while True:
    
    img_w=cv2.imread("exm.png")
    ret, frame = video_capture.read()
    return_value,ima_from_vid=video_capture.read()
    if w==1 :
   	 cv2.imshow("window2",frame)
   	 text=tess.image_to_string(ima_from_vid)
    else:
   	 cv2.imshow('window1',img_w)
   	 text=tess.image_to_string(img_w)
    print(text)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if cv2.waitKey(20) & 0xFF == ord('i'):
        w=0
        cv2.destroyAllWindows()
    if cv2.waitKey(20) & 0xFF == ord('c'):
       w=1
       cv2.destroyAllWindows()

 

video_capture.release()
cv2.destroyAllWindows()
