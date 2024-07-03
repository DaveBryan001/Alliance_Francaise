from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django's User model
    membership_type = models.CharField(max_length=100)  # Type of membership
    membership_start = models.DateField()  # Start date of membership
    membership_end = models.DateField()  # End date of membership

    def __str__(self):
        return self.user.username


class Course(models.Model):
    name = models.CharField(max_length=200)  # Name of the course
    description = models.TextField()  # Detailed description of the course
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the course
    duration = models.CharField(max_length=100)  # Duration of the course
    start_date = models.DateField()  # Start date of the course
    end_date = models.DateField()  # End date of the course
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-filled creation date
    updated_at = models.DateTimeField(auto_now=True)  # Auto-filled last update date

    def __str__(self):
        return self.name
    
class Event(models.Model):
    name = models.CharField(max_length=200)  # Name of the event
    description = models.TextField()  # Detailed description of the event
    date = models.DateField()  # Date of the event
    location = models.CharField(max_length=200)  # Location of the event
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Optional: price of the event
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-filled creation date
    updated_at = models.DateTimeField(auto_now=True)  # Auto-filled last update date

    def __str__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=200)  # Name of the resource
    description = models.TextField()  # Detailed description of the resource
    file = models.FileField(upload_to='resources/')  # File upload path
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Auto-filled upload date

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=200)  # Name of the person giving the testimonial
    testimonial = models.TextField()  # The testimonial content
    date = models.DateField(auto_now_add=True)  # Auto-filled date of testimonial

    def __str__(self):
        return self.name
    

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    membership_type = models.CharField(max_length=100)  # Type of membership
    membership_start = models.DateField()  # Start date of membership
    membership_end = models.DateField()  # End date of membership

    def __str__(self):
        return self.user.username




