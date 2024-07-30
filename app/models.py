from django.db import models

# Create your models here.
class students(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    location = models.CharField(max_length=20, default="Nairobi")

    def __str__(self):
        return self.name

