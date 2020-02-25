from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage),
    path('cep/', views.cep),
    path('cidadesufs/', views.cidadesufs),
    path('filmes/', views.filmes)
]
