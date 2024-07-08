from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import UserCreateView, email_verification, reset_password

from .apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('reset_password/', reset_password, name='reset_password'),
]


