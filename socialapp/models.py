from django.db import models

# Create your models here.
STATUS_CHOICES = (('waiting','WAITING'),('confirm', 'CONFIRM'),('rejected','REJECTED'))
class contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.IntegerField()
    msg=models.TextField()
    postdate= models.DateTimeField(auto_now_add=True)

class Data(models.Model):
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=200,blank=True)
    postdate= models.DateTimeField(auto_now_add=True)
    video= models.FileField(upload_to='videos/', null=True,blank=True, verbose_name="")
    photo=models.ImageField(upload_to='photos/',blank=True)
    camera=models.ImageField(upload_to='photos/',blank=True)
    msg=models.TextField()
    seen=models.IntegerField(default=1)
    likes=models.IntegerField(default=0)
    unlike=models.IntegerField(default=0)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES, default='waiting')
