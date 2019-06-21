from django.db import models
from django.conf import settings
from django.contrib.auth.models import  AbstractUser


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profPic = models.ImageField(upload_to="user_profiles", blank=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    phone_number = models.CharField(max_length=13, default='0712345678')


    # def __str__(self):
    #     return "User profile for {}". format()
    #



# Create your models here.
