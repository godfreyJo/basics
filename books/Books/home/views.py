from django.shortcuts import render, redirect
from .models import Book, User, Borrower
from .forms import BookForm, BorrowerModelForm, BookModelForm

# Create your views here.


def home(request):
    return render(request, 'home.html')

def allbooks(request):
    books = Book.objects.all()
   
    context = {  
    "books":books
    }
    return render(request, 'books.html', context)

def book_details(request, pk):
    book = Book.objects.get(id=pk)
    context = {
    "book":book
    }
    
    return render(request, 'bookDetailed.html', context)

def create_book(request):
    form = BookForm()
    if request.method == 'POST':
        print('receiving a post request') 
        form = BookForm(request.POST)
        if form.is_valid():
           
            Book_Title = form.cleaned_data['Book_Title']
            ISBN_Number = form.cleaned_data['ISBN_Number']
            DatePublished = form.cleaned_data['DatePublished']
            category = form.cleaned_data['category']
            author = form.cleaned_data['author']
            status = form.cleaned_data['status']
            
            Book.objects.create(
                Book_Title=Book_Title,
                ISBN_Number=ISBN_Number,
                DatePublished=DatePublished,
                category=category,
                author=author,
                status=status)
           
            return redirect('/books')

                  
       

    context = {
        'form': form
    }

    return render(request, 'bookCreate.html', context)


def new_borrower(request):
    form = BorrowerModelForm()
    if request.method == 'POST':
        form = BorrowerModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books')
    context = {
        'form': form
    }

    return render(request, 'borrowerCreate.html', context)


def book_update(request, pk):
    book = Book.objects.get(id=pk)
    form = BookModelForm(instance=book)
    
    if request.method == 'POST':
        form = BookModelForm(request.POST, instance=book)        
        if form.is_valid():
            form.save()
            
            return redirect('/books')

    context = {
        'form': form,
        'book': book
    }
    return render(request, 'bookUpdate.html', context=context)



   