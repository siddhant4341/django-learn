from django.db import models

# Create your models here.

#TEACHER TABLE------------------
class Teacher(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.BigIntegerField()

    def __str__(self) -> str:
        return self.Firstname


#CRUD APPLICATION---------------

#model for User registration.
class User(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.BigIntegerField()
    Password = models.CharField(max_length=50)


#IMAGE UPLOADING-----------------
class ImageData(models.Model):
    Imagename = models.CharField(max_length=50)
    Image = models.ImageField(upload_to="img/")