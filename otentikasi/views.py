from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

class otentikasiLogin(LoginView):
    template_name = 'login.html'

redirect_authenticated_user = True

class otentikasiLogout(LogoutView):
    def logout_view(selfrequest):
        logout(request)
    template_name = 'login.html'
    next_page = 'scanner'