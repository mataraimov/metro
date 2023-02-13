from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PostCategory(models.Model):
    name=models.CharField(max_length=128,unique=True)
    description=models.TextField(null=True,blank=True)

    def __repr__(self):
        return self.name

# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=255,null=False,blank=False)
    content=models.CharField(max_length=255,null=False,blank=False)
    post_date=models.DateTimeField(default=timezone.now)
    category=models.ForeignKey(to=PostCategory,on_delete=models.CASCADE)
    images = models.ImageField('images')
    def __repr__(self):
        return self.title

