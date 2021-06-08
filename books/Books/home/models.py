from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
	pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
    


class Book(models.Model):
    Book_Title = models.CharField(max_length=255)
    ISBN_Number = models.IntegerField()
    DatePublished = models.DateField()
    category = models.CharField(max_length=255)
    author = models.CharField(max_length=255)    
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.Book_Title)

class Borrower(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    booksBorrowed = models.IntegerField()
    dateBorrowed = models.DateField()
    dateToReturn = models.DateField()
    status = models.BooleanField(default=False)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    
   
post_save.connect(post_user_created_signal, sender=User)

        




