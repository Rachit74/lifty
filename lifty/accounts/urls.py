from django.urls import path

from . import views

urlpatterns = [
    path('', views.accounts_home, name='account-home'),
    path('register/', views.register, name='register'),
]