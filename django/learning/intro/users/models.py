from django.db import models

class User(models.Model):
    forename   = models.CharField(max_length=100)
    surname    = models.CharField(max_length=100)
    email      = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email
