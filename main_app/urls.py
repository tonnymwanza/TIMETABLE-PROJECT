from django.urls import path

from . views import HomeView
# my urls

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]