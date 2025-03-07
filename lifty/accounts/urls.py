from django.urls import path

from . import views

urlpatterns = [
    path('', views.accounts_home, name='account-home'),
    path('profile/', views.user_profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]