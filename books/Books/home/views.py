from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book, User, Borrower
from .forms import BookForm, BorrowerModelForm, BookModelForm, CustomUserCreationForm

# Create your views here.


#we are going to replace the function based views into classBased views
class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')



class LandingPageView(TemplateView):
    template_name = 'landing.html'



def landing_page(request):
    return render(request, 'landing.html')


class BookListView(LoginRequiredMixin, ListView):
    template_name = 'books.html'
    queryset = Book.objects.all()
    context_object_name = 'books'


def allbooks(request):
    books = Book.objects.all()   
    context = {  
    "books":books
    }
    return render(request, 'books.html', context)

class BookDetailView(LoginRequiredMixin, DetailView):
    template_name = 'bookDetailed.html'
    queryset = Book.objects.all()
    context_object_name = 'book'

def book_details(request, pk):
    book = Book.objects.get(id=pk)
    context = {
    "book":book
    }
    
    return render(request, 'bookDetailed.html', context)

class BookCreateView(LoginRequiredMixin, CreateView):
    template_name = 'bookCreate.html'
    form_class = BookForm

    def get_success_url(self):
        return reverse('books:book-list')
    
    def form_valid(self, form):
        # TODO: send email
        send_mail()
        return super(BookCreateView, self).form_valid(form)
    


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

class BookUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'bookUpdate.html'
    queryset = Book.objects.all()
    form_class = BookForm

    def get_success_url(self):
        return reverse('books:book-list')

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

class BookDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'bookDelete.html'
    form_class = BookForm

    def get_success_url(self):
        return reverse('books:book-list')

def book_delete(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect('/books')
    

   