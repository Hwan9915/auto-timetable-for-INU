from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    major = models.CharField(max_length=50)
    year = models.IntegerField()
    classification = models.CharField(max_length=20)
    course_code = models.CharField( max_length=20)
    course_name = models.CharField(max_length=100)
    professor = models.CharField(max_length=50)
    timetable_period = models.CharField(max_length=100)
    timetable_time = models.CharField(max_length=100)
    credits = models.IntegerField()
    class_type = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.major}, {self.year}학년, {self.course_name}"
    
class Major(models.Model):
    id = models.AutoField(primary_key=True)
    major_name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.major_name}"