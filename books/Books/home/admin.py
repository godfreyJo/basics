from django.contrib import admin
from .models import User, Borrower, Book

# Register your models here.


admin.site.register(User)
admin.site.register(Borrower)
admin.site.register(Book)



