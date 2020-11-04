import cv2
import pyautogui
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml') 
c=0
def detect(gray, frame,d,c): 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
    
    for (x, y, w, h) in faces: 
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2) 
        roi_gray = gray[y:y + h, x:x + w] 
        roi_color = frame[y:y + h, x:x + w] 
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20) 
  
        for (sx, sy, sw, sh) in smiles: 
            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
            if(c!=d-1):
            	pyautogui.screenshot("ss/sm.png")
            	c=d
            
    #print(c)
    return frame,c
video = cv2.VideoCapture(0) 
d=0
while True: 
     
    a, frame = video.read()  # used a as a throwaway variable
    d=d+1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   
    feed,c = detect(gray, frame,d,c)    
    cv2.imshow('Video', feed)  
    if cv2.waitKey(1) & 0xff == ord('e'):                
        break
   
video.release()                                  
cv2.destroyAllWindows() 
