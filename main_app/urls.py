from django.urls import path
from . import views
from . views import HomeView
from . views import RegistrationSuccessfulView
# my urls

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('registration_successful', RegistrationSuccessfulView.as_view(), name='registration_successful'),
]