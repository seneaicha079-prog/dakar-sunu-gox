from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('a-propos/', views.a_propos, name='apropos'),
    path('lieux/', views.lieux, name='lieux'),
    path('histoires/', views.histoires, name='histoires'),
    path('loisirs/', views.loisirs, name='loisirs'),
]