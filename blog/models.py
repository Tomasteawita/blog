from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
    
class Tag(models.Model):
    name = models.CharField(max_length=65)
    date_creation = models.DateTimeField()
    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=256)
    body = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='images',null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    date = models.DateTimeField(null=True)
    state = models.BooleanField('Active',default=False)
    
    def __str__(self):
        return f'Post: {self.title}'

class Comentaries(models.Model):
    text = models.CharField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,null=True,blank=True)
    