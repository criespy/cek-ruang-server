from django.views.generic import ListView, UpdateView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class pilihRuangServer(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = "pilihRuangServer.html"
