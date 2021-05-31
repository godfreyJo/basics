from django.urls import path
from . import views

urlpatterns = [
    
    
    path('', views.home, name='home'),
    path('books/', views.allbooks, name='allbooks'),
    path('<int:pk>/', views.book_details, name='book_details'),
    path('<int:pk>/update/', views.book_update, name='book_update'),
    path('create/', views.create_book, name='create_book'),
    path('new_borrower/', views.new_borrower, name='new_borrower')
   

    
]
