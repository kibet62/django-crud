from django.db import models



class Students(models.Model):
    name = models.CharField
    email = models.EmailField
    age = models.IntegerField
    gender = models.CharField


    def __str__(self):
        return self.name