from django.urls import path, include

from app1 import views

urlpatterns = [

path('<int:pk>/', views.snippet_list, name='snippet_list'),
]
