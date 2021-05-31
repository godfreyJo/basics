from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
	pass


class Book(models.Model):
    bookTitle = models.CharField(max_length=255)
    bookIsbn_Number = models.IntegerField()
    bookDatePublished = models.DateField()
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    borrower = models.ForeignKey("Borrower", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.bookTitle)

class Borrower(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	booksBorrowed = models.IntegerField()
	dateBorrowed = models.DateField()
	dateToReturn = models.DateField()
	status = models.CharField(max_length=10)

	def __str__(self):
		return str(self.user)

	



