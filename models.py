from django.db import models
import datetime
# Create your models here.

class Register(models.Model):
    Student_name = models.CharField(max_length=50,default="")
    Student_id = models.CharField(primary_key=True,max_length=50,default="")
    phone=models.CharField(max_length=50,default="")
    image=models.ImageField(upload_to="face/images/" ,null=True,blank=True)

    def __str__(self):
            return self.Student_name


class Attendance(models.Model):
    Student_id = models.CharField(max_length=50,default="")
    date=models.DateField(("date"), default=datetime.date.today)
    status=models.CharField( max_length=50,default="")
    time=models.CharField( max_length=50,default="")

    def __str__(self):
            return self.Student_id





