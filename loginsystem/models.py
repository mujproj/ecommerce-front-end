from django.db import models

# Create your models here.
class newuser(models.Model):
    username = models.CharField(max_length = 50, unique=True)
    emailID = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.username

