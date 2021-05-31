from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
	pass


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
	status = models.CharField(max_length=10)

	def __str__(self):
		return str(self.user)

	



