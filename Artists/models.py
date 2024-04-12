from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Artists(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self) -> str:
        return self.Name
    

