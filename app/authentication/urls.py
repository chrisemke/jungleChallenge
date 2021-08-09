from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login.as_view()),
    path('sign-up/', views.Signup.as_view())
]
