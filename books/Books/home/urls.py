from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
from . import views


app_name = "home"

urlpatterns = [
    
    
    # path('', views.home, name='home'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book-details'),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('create/', BookCreateView.as_view(), name='create-book'),
    path('new_borrower/', views.new_borrower, name='new-borrower')
   

    
]
