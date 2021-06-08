from django import forms
from .models import Borrower, Book

class BorrowerModelForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = (
            'user',
            'booksBorrowed',
            'dateBorrowed',
            'dateToReturn',
            'status',
            )

class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'Book_Title',
            'ISBN_Number',
            'DatePublished',
            'category',
            'author',
            'status'


        )


class BookForm(forms.Form):
    Book_Title = forms.CharField()
    ISBN_Number = forms.IntegerField()
    DatePublished = forms.DateField()
    category = forms.CharField()
    author = forms.CharField()
    status = forms.BooleanField()


    
