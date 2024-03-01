import os
import face_recognition
import cv2

path='dataset'
subdir=os.listdir(path)
img = face_recognition.load_image_file("NewPicture.jpg")
unknown_encode=face_recognition.face_encodings(img)[0]

for image in subdir :
    f=os.path.join(path,image)
    known_image=face_recognition.load_image_file(f)
    known_encode=face_recognition.face_encodings(known_image)[0]
    result=face_recognition.compare_faces([unknown_encode],known_encode)
    if result[0]==True:
        name=image.split(".")[0]
        print(name)
    else:
        print("Unknown ") 