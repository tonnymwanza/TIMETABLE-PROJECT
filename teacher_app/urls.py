from django.urls import path

from . views import TeacherView
# my urls

urlpatterns = [
    path('teacher', TeacherView.as_view(), name='teacher'),
]