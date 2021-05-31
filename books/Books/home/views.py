from django.shortcuts import render
from .models import Book, User, Borrower

# Create your views here.


def allbooks(request):
    books = Book.objects.all()
   
    context = {  
    "books":books
    }
    return render(request, 'home.html', context)

def detailBook(request, pk):
    book = Book.objects.get(id=pk)
    context = {
    "book":book
    }
    
    return render(request, 'bookDetailed.html', context)

 


   