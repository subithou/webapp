from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.id + self.first_name + self.last_name