from turtle import title
from unicodedata import category, name
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __str__(self):
        return self.user.username

# Create the book model with name, description, author
class Book(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    author = models.CharField(max_length=50)

    def __str__(self): 
        return str(self.name)

# Create review model with information about the review
class Review(models.Model):
    time = models.DateTimeField()
    comments = models.CharField(max_length=300,blank=True)
    ratings = models.IntegerField(default=5)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self): 
        return str(self.ratings)



