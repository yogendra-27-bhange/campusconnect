from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=50)
    enrollment_date = models.DateField()
    profile_pic = models.ImageField(upload_to='students/', blank=True, null=True)

    def __str__(self):
        return self.name
