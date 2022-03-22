from django.urls import path, include

from app1 import views
from app1.views import SnippetView

urlpatterns = [

# path('<int:pk>/', views.snippet_list, name='snippet_list'),
path('',SnippetView.as_view()),
path('<int:pk>/',SnippetView.as_view()),
]
