from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField('Title', max_length=1024)
    description=models.TextField(null=True,blank=True)
    created_at=models.DateField(auto_now_add=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='post')

    def __str__(self) -> str:
        return self.title

class PostImage(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='image')
    image=models.ImageField(null=True,blank=True,upload_to='primary/images')


class Review(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='review')
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='review')
    description=models.TextField() 
    date=models.DateField(auto_now_add=True)

class Reply(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='reply')
    review=models.ForeignKey(Review,on_delete=models.CASCADE,related_name='reply')
    reply=models.CharField(max_length=70)
    date=models.DateField(auto_now_add=True)
    

