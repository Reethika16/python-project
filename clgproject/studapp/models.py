from django.db import models

# Create your models here.
class course(models.Model):
    courseid = models.IntegerField(primary_key=True)
    coursename = models.CharField(max_length=30)
    coursefee=models.IntegerField(default=10000)


    def __str__(self):
        return f'{self.courseid}-{self.coursename}'


class student(models.Model):
    stuid=models.IntegerField(primary_key=True)
    stuname=models.CharField(max_length=30)
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    location=models.CharField(max_length=20)


    def __str__ (self):
        return f'{self.stuid}-{self.stuname}-{self.course}'


class staff(models.Model):
    staffid = models.IntegerField(primary_key=True)
    staffname = models.CharField(max_length=30)
    location = models.CharField(max_length=20)

    def __str__ (self):
        return f'{self.staffid}-{self.staffname}'


