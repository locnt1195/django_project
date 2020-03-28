from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('infor/', views.infor, name='blog-infor'),
    path('about/', views.about, name='blog-about'),
]
