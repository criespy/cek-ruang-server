from django.urls import path
from . import views

urlpatterns = [
    path('', views.pilihRuangServer.as_view(), name='pilihruangserver'),
]