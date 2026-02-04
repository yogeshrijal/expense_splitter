from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
 ROLES_CHOICES=[
    ('admin','Admin'),
    ('user','User'),

    ]
 role=models.CharField(choices=ROLES_CHOICES,default='user',)
 contact=models.IntegerField()
 address=models.CharField(max_length=100)
 profile_picture=models.ImageField( upload_to='User/', null=True,blank=True)




 def __str__(self):
  return f"{'self.username'}:{'self.role'}"
 

 
 

