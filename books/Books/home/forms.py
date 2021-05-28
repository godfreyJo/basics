from django import forms


class Book(forms.Form):
    bookTitle = forms.CharField()
    bookIsbn_Number = forms.IntegerField()
    bookDatePublished = forms.DateField()
    author = forms.CharField()

    