from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.allbooks, name='allbooks'),
    path('<pk>/', views.detailBook, name='detailBook'),

    
]
