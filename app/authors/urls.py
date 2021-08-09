from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.AuthorsView.as_view()),
    path('authors/<int:pk>', views.AuthorsView.as_view())
]
