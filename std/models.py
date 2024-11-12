from django.db import models

# Create your models here.

class Std(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=30)
    age=models.IntegerField()


class Club(models.Model):
    name=models.CharField(max_length=30)
        
