'''import cv2
import face recognition as fr
import numpy as np

url = 'http://26.75.163.191:8080/video'
video=cv2.VideoCapture(url)

Hitendra_image = fr . load_image_file("HUD\Hitendra Pal.jpeg")
Hitendra_face_encoding = fr.face_encodings(Hitendra_image)[0]

know_face_encondings = (Hitendra_face_encoding)
know_face_names = ["Hitendra"]


while True:
    ret,frame=video.read()

    rbg_frame = frame[:,  :,  ::-1]

    face_locations = fr.face_locations[rbg_frame]
    face_encodings = fr.face_encodings[rbg_frame,  face_locations]

    for (top, right, bottom, left), face_encodings in zip(face_locations, face_encodings):

        matches = fr.compare_faces(know_face_encondings,  face_encodings)

        name = "unknown"

        face_distances = fr.face_distance(know_face_encondings, face_encodings)

        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
             name = know_face_names[best_match_index]
    
        cv2.rectangle(frame, (left,top), (right,bottom), (0, 0, 255), 2)

        cv2.rectangle(frame,(left,bottom -35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, name,  (left + 6, bottom - 6), font, 1.0, (255, 255, 255),  1) 
    
    cv2.imshow("Webcam_facerecognition",  frame)
   
    if  cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()   '''


# face recognition 2nd method 

import cv2
import os 

URL='http://10.132.66.12:8080/video'
video=cv2.VideoCapture(URL)

facedetect=cv2.CascadeClassifier('haarcasscade_frontalface_default.xml')

count=0

nameID=str(input("Enter Your Name:  ")).lower()

path='HUD/images/' +nameID

isExist = os.path.exists(path)

if  isExist:
    print("Name Already Taken ")
    nameID=str(input(" Enter Your Name Again:   "))
else:
    os.makedirs(path)

while True :
    ret,frame=video.read()
    faces=facedetect.detectMultiScale( frame,1.3,  5)
    for x,y,w,h in faces:
        count=count+1
        name='HUD/image/'+nameID+'/'+ str(count) +'.jpg'
        print('Creating Images................'+name)
        cv2.imwrite(name, frame[y:y+h,x:x+w])
        cv2.rectangle(frame, (x,y), (x+w,  y+h),  (0,255,0),  3)
    cv2.imshow("WindowFrame" ,  frame)
    cv2.waitKey(1)
    if count>500:
        break
video.release()
cv2.destroyAllWindows()
         
    
        

