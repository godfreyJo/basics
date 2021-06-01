from django.urls import path
from . import views


app_name = "home"

urlpatterns = [
    
    
    # path('', views.home, name='home'),
    path('books/', views.allbooks, name='book-list'),
    path('<int:pk>/', views.book_details, name='book-details'),
    path('<int:pk>/update/', views.book_update, name='book-update'),
    path('<int:pk>/delete/', views.book_delete, name='book-delete'),
    path('create/', views.create_book, name='create-book'),
    path('new_borrower/', views.new_borrower, name='new-borrower')
   

    
]
