from django.urls import path
from .views import HomeView, LoginView, RegistrationView

urlpatterns = [
        path("", HomeView.as_view(), name='home'),
        path("register", RegistrationView.as_view(), name='register'),
        path("login", LoginView.as_view(), name='login'),
        
        ]
