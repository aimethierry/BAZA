from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import datetime 
from django.dispatch import receiver
import datetime
from django.db.models import Q






class Post(models.Model):
    author = models.ForeignKey('auth.User', null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    document = models.FileField(upload_to='documents/', blank=True)

    Choices=(
        ('Chemistry','CHEM') ,
        ('Physics ','PHY'),       
        ('Mathematics','MATH'),
        ('Biology','BIO'),
        ('Computer' ,'CS'),
        ('History','HIS'),
        ('Economics','ECON'),
        ('Literature','LIT'),
        ('Geography','GEO'),
        ('Entrepreneurship','ENT')
  
        )

    field=models.CharField(max_length=100 ,choices=Choices,default='all')
    created_date = models.DateTimeField(
            default=timezone.now)
    
    published_date = models.DateTimeField(
            blank=True, null=True)
    check_date=models.DateField(default=datetime.date.today)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Answer(models.Model):
    post = models.ForeignKey('myblog.Post', related_name='answers', null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.text

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='media')

class Notification(models.Model):
    post = models.ForeignKey('myblog.Post', related_name='notifications',null=True)
    answer = models.ForeignKey('myblog.Answer', related_name='answer_notifications',null=True)
    title=models.CharField(max_length=250)
    message=models.TextField()
    created_date=models.DateField(default=datetime.date.today)
    created_time = models.DateTimeField(
            default=timezone.now)





@receiver(post_save,sender=Post)
def tell_new_post(sender,**kwargs):
    if kwargs.get('created',False):
        Notification.objects.create(post=kwargs.get('instance'),title=" posted something!", message="If you know the answer please provide it!")





@receiver(post_save,sender=Answer)
def tell_new_answer(sender,**kwargs):
    if kwargs.get('created',False):
        Notification.objects.create(answer=kwargs.get('instance'),title="'s post was answered!:", message="was it help full?")


class Project(models.Model):
    first_name  = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    Choices=(
        ('Science','science') ,
        ('Arts ','arts'),       
        ('skills','skills'),
        )
    field=models.CharField(max_length=100 ,choices=Choices,default='all')
    text = models.TextField()
    image = models.ImageField(upload_to= 'documents/',null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    
    published_date = models.DateTimeField(
            blank=True, null=True)

class School(models.Model):
    adress = models.CharField(max_length=300)
    school_email = models.CharField(max_length=300)
    school_name = models.CharField(max_length=300)

class Teacher(models.Model):
    bio = models.TextField(max_length=500, blank=True,default=True)
    location = models.CharField(max_length=30, blank=True,null=True)
    birth_date = models.DateField(blank=True)
    image = models.FileField(upload_to = 'documents/',blank=True, default=True)



class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True)
    text = models.TextField(null=True)
    user = models.ForeignKey('auth.User',null=True, related_name='documents')
    created_date = models.DateTimeField(
            default=timezone.now, null=True)
    
    published_date = models.DateTimeField(
            blank=True, null=True)
    check_date=models.DateField(default=datetime.date.today,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()




class Comment(models.Model):
    post = models.ForeignKey('myblog.Post', related_name='comments', null=True)
    author = models.CharField(max_length=200, null=True)
    text = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text