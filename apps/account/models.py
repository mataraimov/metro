from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # email = models.CharField(max_length=255,null=False,blank=False,unique=True)
    name = models.CharField(max_length=255,null=False,blank=False)
    second_name = models.CharField(max_length=255,null=False,blank=False)

    def __repr__(self):
        return self.email