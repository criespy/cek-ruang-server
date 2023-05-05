from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

class otentikasiLogin(LoginView):
    template_name = 'login.html'
