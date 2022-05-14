from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from django.shortcuts import redirect, render


# Create your views here.

class RegistrationView(FormView):
    template_name = 'form.html'
    form_class = UserForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
        

class LoginView(FormView):
    template_name = 'form.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
           login(self.request, user)
           self.success_url = '/dashboard'
           
        else:
           messages.error(self.request,"Invalid username or password.")
           self.success_url = '/login'
        return super().form_valid(form)
    

def logout_view(request):
    logout(request)
    return redirect('/')

















