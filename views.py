from django.shortcuts import render
from http.client import HTTPResponse
from django.http import HttpResponse
from face.models import Register
from face.models import Attendance
import cv2
import os
import time
import face_recognition

# Create your views here.

def start(request):
    return render(request,'start.html')

def register(request):
    return render(request,'register.html')

def saving(request):
    
    vid = cv2.VideoCapture(0)
    while(True):
        ret,frame = vid.read()
        cv2.imshow('Capture Your Photo',frame)
        if cv2.waitKey(15) & 0xFF == ord(' '):
            s = time.time()
            cv2.imwrite("C:/Users/HARSHIT/Desktop/Attendance/Django_part/attend/face/images/Pic%s.jpg" %s,frame)
            cv2.imwrite("NewPicture.jpg",frame)
            break
    vid.release()
    cv2.destroyAllWindows()

    if request.method=="POST":
        name=request.POST.get('name')
        id=request.POST.get('id')
        number=request.POST.get('number')
        en=Register(Student_name=name,Student_id=id,phone=number,image="NewPicture.jpg")
        en.save()
    return render(request,'after_register.html')
    

def attendence_form(request):
    return render(request,'attendance.html')


def attendence(request):
    vid = cv2.VideoCapture(0)
    while True :
        ret , frame = vid.read()
        cv2.imshow('Capture Your Photo',frame)
        if cv2.waitKey(15) & 0xFF == ord(' '):
            cv2.imwrite("NewPicture.jpg",frame)
            break
    vid.release()
    cv2.destroyAllWindows()

    path='C:/Users/HARSHIT/Desktop/Attendance/Django_part/attend/face/images'
    subdir=os.listdir(path)
    img = face_recognition.load_image_file("NewPicture.jpg")
    unknown_encode=face_recognition.face_encodings(img)[0]

    cheak=False

    for image in subdir :
        f=os.path.join(path,image)
        known_image=face_recognition.load_image_file(f)
        known_encode=face_recognition.face_encodings(known_image)[0]
        result=face_recognition.compare_faces([unknown_encode],known_encode)
        if result[0]==True:
            name=image.split(".")[0]
            print(name)
            cheak=True
            break
        

    if cheak==True:
        
        if request.method=="POST":

            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)

            id=request.POST.get('id')
            date=request.POST.get('date')
            en=Attendance(Student_id=id,date=date,status="Present",time=current_time) 
            en.save()
        mydata=Register.objects.filter(Student_id=id)
        attendata=Register.objects.all()
        
        if(len(mydata) == 0):
            print("Yes")
            tagy="Unregistered"
            dict={'mark':tagy}
            return render(request,'falseattend.html',dict)
            
        for i in mydata:
            print(i.Student_name)
            print(i.phone)
            print(i.Student_id)
            print(date)
            
        dict={'mark':mydata,
              'time':current_time,
              'daty':date
        }
        return render(request,'trueattend.html',dict)    
        
    else:
        tagy="Unregistered"
        dict={'mark':tagy}
        return render(request,'falseattend.html',dict)
        

         
