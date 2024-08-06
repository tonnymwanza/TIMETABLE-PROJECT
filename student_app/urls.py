from django.urls import path

from . views import StudentView
# my urls

urlpatterns = [
    path('student', StudentView.as_view(), name='student'),
]