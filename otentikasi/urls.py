from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.otentikasiLogin.as_view(), name='login'),

]