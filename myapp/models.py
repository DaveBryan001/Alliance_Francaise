from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django's User model+
    membership_type = models.CharField(max_length=100)
    membership_start = models.DateField() 
    membership_end = models.DateField()

    def __str__(self):
        return self.user.username


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Event(models.Model):
    name = models.CharField(max_length=200)  
    description = models.TextField()  
    date = models.DateField() 
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()  
    file = models.FileField(upload_to='resources/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now_add=True)


class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    testimonial = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    





